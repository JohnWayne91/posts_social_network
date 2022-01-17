from django.contrib import admin

from .models import Like, Post, UserActivity


admin.site.register(Like)
admin.site.register(Post)
admin.site.register(UserActivity)
