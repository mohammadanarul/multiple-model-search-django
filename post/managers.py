from django.db import models
from django.db.models import Q


class PostQueryset(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(slug__icontains=query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQueryset(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class LessonQueryset(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(slug__icontains=query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs


class LessonManager(models.Manager):
    def get_queryset(self):
        return LessonQueryset(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)
