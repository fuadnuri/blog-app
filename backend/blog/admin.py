from django.contrib import admin
from .models import (Post,LikeComment,Comment)
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'bio')


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'avatar', 'bio')
