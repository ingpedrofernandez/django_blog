from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog-post-detail', args=[str(self.id)])