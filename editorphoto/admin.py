from django.contrib import admin
from .models import UserImage, ImageCategory



@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = ("user", "uploaded_at")
    search_fields = ("user", )
    ordering = ("-uploaded_at", )



@admin.register(ImageCategory)
class ImageCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    
    
