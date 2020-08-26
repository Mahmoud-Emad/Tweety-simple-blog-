from django.contrib import admin
from .models import Post,category,Profile,Comment



admin.site.register(category)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)