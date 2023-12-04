from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.contrib.auth.models import AbstractUser
from drf import settings


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, surname, birthday, gender, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            birthday=birthday,
            gender=gender
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.model(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Емайл',
        max_length=255,
        unique=True,
    )
    
    name = models.CharField('Имя', max_length=150, blank=True)
    surname = models.CharField('Фамилия', max_length=150, blank=True)
    gender = models.CharField('Пол', max_length=7, default='Мужской')
    birthday = models.DateField('Дата рождения', max_length=8, null=True)
    is_active = models.BooleanField('Активный', help_text='Отметьте, если пользователь должен считаться активным. ''Уберите эту отметку вместо удаления учётной записи.', default=True)
    is_staff = models.BooleanField('Статус персонала', help_text='Отметьте, если пользователь может входить в ''административную часть сайта.', default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
    
    def full_name(self):
        return f'{self.name} {self.surname}' if self.name and self.surname else self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
