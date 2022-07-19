from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User
# Register your models here.

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['email', 'username', 'is_staff']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ['email', 'username']
    ordering = ['email']

admin.site.register(User, UserAdmin)

