# -*- coding: utf-8 -*-
from django.contrib import admin
from Blog.models import Post # наша модель из blog/models.py

admin.site.register(Post)
# Register your models here.
