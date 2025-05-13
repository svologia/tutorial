from django.contrib import admin
from .models import Snippet, Tag, Comment

admin.site.register(Snippet)
admin.site.register(Tag)
admin.site.register(Comment)