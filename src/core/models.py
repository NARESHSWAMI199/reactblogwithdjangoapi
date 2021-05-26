from django.db import models
from django.db.models.query_utils import select_related_descend


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()


    def __str__(self):
        return self.title
