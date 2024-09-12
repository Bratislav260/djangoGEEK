from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    creates_at = models.DateTimeField(auto_created=True, null=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
