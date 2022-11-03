from django.conf import settings
from django.db import models
from django.utils.text import slugify

from .managers import LessonManager, PostManager


# course.post
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    publish_date = models.DateTimeField(
        auto_now_add=False, auto_now=False, null=True, blank=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = PostManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


# courses.lesson
class Lesson(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    featured = models.BooleanField(default=False)
    publish_date = models.DateTimeField(
        auto_now_add=False, auto_now=False, null=True, blank=True
    )
    objects = LessonManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Lesson, self).save(*args, **kwargs)


# profiles.profile
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Profile, self).save(*args, **kwargs)
