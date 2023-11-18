from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import MyUser
from django.contrib.auth.models import Group


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    model = MyUser
    list_display = ['email', 'first_name',
                    'last_name', 'phone', 'gender', 'group', 'age', 'date_joined']
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    "email",
                    "first_name",
                    "last_name",
                    "phone",
                    "gender",
                    "group",
                    "age",
                    "date_joined"
                )
            }
        )
    )
