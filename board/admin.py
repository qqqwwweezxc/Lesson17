from django.contrib import admin
from . import models


admin.site.register(models.UserProfile)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(models.Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'user', 'is_active', 'created_at')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'ad', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)