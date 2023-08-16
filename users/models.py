from django.db import models
from django.contrib.auth.models import AbstractUser
GENDER_CHOICES = (
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Мужчина', 'Мужчина'),
    ('Женщина', 'Женщина'),
)

class CustomUser(AbstractUser):
    
    first_name = models.CharField(
        'Имя',
        max_length=255
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=255
    )
    gender = models.CharField(
        'Пол',
        max_length=7, 
        choices=GENDER_CHOICES, default='MEN'
    )
    age = models.IntegerField(
        'Возраст',
        null=True
    )
