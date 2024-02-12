from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import MyUser
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import (
    AdminPasswordChangeForm
)
from users.forms import MyUserChangeForm, MyUserCreationForm

class MyUserAdmin(BaseUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    change_password_form = AdminPasswordChangeForm
    
    list_display = ('email', )
    list_filter = ('is_active', 'is_staff', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'surname',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('user_permissions',)

admin.site.register(MyUser)
#admin.site.unregister(Group)