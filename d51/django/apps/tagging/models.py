from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey("Tag", related_name="children", null=True, blank=True)

    object_id = models.PositiveIntegerField(null=True)
    content_type = models.ForeignKey(ContentType, null=True)
    content_object = generic.GenericForeignKey()

    def __unicode__(self):
        if self.parent:
            return "%s > %s" % (self.parent, self.title)
        return self.title
