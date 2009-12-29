from d51.django.apps.tagging.models import Tag
from django.contrib.contenttypes import generic
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    tags=generic.GenericRelation(Tag)

class Post(models.Model):
    title = models.CharField(max_length=50)
    tags=generic.GenericRelation(Tag)

