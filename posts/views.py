from django.shortcuts import redirect, render
from django.http import HttpResponse
from posts.models import Post, Comment
from posts.forms import PostForm2, CommentForm


def testing_view(request):
    return HttpResponse("Привет, мирок")


def main_page(request):
    if request.method == "GET":
        return render(request, "base.html")


def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "posts/post_list.html", context={"post": posts})


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
