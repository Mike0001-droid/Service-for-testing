from django.contrib.auth.forms import UserCreationForm
from users.models import MyUser


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone",
            "gender",
            "group",
            "age",
            "date_joined"
        )
