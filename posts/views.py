from django.shortcuts import redirect, render
from django.http import HttpResponse
from posts.models import Post, Comment
from django.db.models import Q
from posts.forms import PostForm2, CommentForm, SearchForm


def testing_view(request):
    return HttpResponse("Привет, мирок")


def main_page(request):
    if request.method == "GET":
        return render(request, "base.html")


def post_list_view(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        search = request.GET("search")
        posts = Post.objects.all()
        tag = request.GET.getList("tag")
        ordering = request.GET.get("ordering")

        if search:
            posts = posts.filter(Q(title_icontains=search)
                                 | Q(search_icontains=search))

        if tag:
            posts = posts.filter(tags__id__in=tag)

        if ordering:
            posts = posts.order_by(ordering)

        limit = 3
        page = request.GET.get("page", 1)
        page = int(page)
        max_pages = posts.count() / limit

        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (page - 1) * limit
        end = page * limit

        posts = posts[start:end]
        context = {"posts": posts, "form": form,
                   "max_pages": range(1, max_pages + 1)}
        return render(request, "posts/post_list.html", context=context)


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "GET":
        form = CommentForm()
        return render(request, "post/post_detail.html", context={"post": post})

    if request.method == "POST":
        form = CommentForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                "post/post_detail.html",
                context={"post": post, "form": form},
            )
        text = form.cleaned_data.get("text")
        Comment.objects.create(text=text, post=post)
        return redirect(f"/posts/{post.id}/")


def post_creat_view(request):
    if request.method == "GET":
        form = PostForm2()
        return render(request, "posts/post_creat.html", context={"form": form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_creat.html", context={"form": form})

        form.save()
        return redirect("/posts/")
