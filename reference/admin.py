from django.contrib import admin
from .models import Reference

#admin.site.register(Post)
@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'link', 'author', 'created', 'updated')
    list_filter = ('title', 'description', 'link', 'author', 'created', 'updated')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ('created',)
# Register your models here.
