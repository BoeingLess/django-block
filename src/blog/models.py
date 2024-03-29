from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from blog.managers import PublishedManager


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT= 'DRAFT', 'draft'
        PUBLISHED= 'PUB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    status=models.CharField(max_length=20,choices=Status.choices, default=Status.DRAFT)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    approved = PublishedManager()

    class Meta:
        ordering = ['-published']
        indexes = [models.Index(fields=['-published'])]

    def __str__(self):
        return self.title
