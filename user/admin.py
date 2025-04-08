from django.contrib import admin
from .models import Account



@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email")
    search_fields = ("is_active","phone_number")
    list_filter = ("date_created", )
    

