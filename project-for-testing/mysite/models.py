from d51.django.apps.tagging.models import Tag
from django.contrib.contenttypes import generic
from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=100)
    tags=generic.GenericRelation(Tag)

class Post(models.Model):
    title=models.CharField(max_length=100)
    tags=generic.GenericRelation(Tag)

