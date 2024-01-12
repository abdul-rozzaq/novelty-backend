from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Token

class UserAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone']

admin.site.register(User, UserAdmin)
admin.site.register(Token)
