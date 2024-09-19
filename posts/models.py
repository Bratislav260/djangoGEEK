from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="posts")
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    creates_at = models.DateTimeField(auto_created=True, null=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    text = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
