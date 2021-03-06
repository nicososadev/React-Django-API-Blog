from django.contrib import admin

from .models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'status')
    

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
