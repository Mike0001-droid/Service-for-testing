from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from django.contrib.auth.models import Group


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'gender', 'age', 'is_staff']
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    "first_name",
                    "last_name",
                    "gender",
                    "age",
                    "group"  
                )
            }
         )
    )

