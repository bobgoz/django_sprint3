from django.contrib import admin

from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'created_at',
        'is_published',
    )
    list_editable = (
        'is_published',

    )
    search_fields = ('title',)
    list_filter = (
        'title',
        'slug',
        'created_at',
        'is_published',
    )
    list_display_links = ('title',)


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    list_filter = (
        'name',
        'created_at',
        'is_published',
    )
    list_display_links = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'category',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title',)
    list_filter = (
        'category',
        'is_published',
    )
    list_display_links = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.empty_value_display = 'Не задано'
