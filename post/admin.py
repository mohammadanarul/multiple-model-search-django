from django.contrib import admin

from post.models import Lesson, Post, Profile

admin.site.register([Lesson, Post, Profile])
