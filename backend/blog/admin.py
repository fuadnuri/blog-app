from django.contrib import admin
from .models import (Post,Comment)
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content','date_posted')


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):    
    list_display = ('author', 'post', 'comment')
