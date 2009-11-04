from d51.django.apps.tagging.models import Tag
from django.contrib import admin

class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'parent'),
        }),
    )

admin.site.register(Tag, TagAdmin)

