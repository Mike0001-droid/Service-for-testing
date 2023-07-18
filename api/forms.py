from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    login = forms.CharField(
        forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'login'
            }), help_text='Логин')
    
    password = forms.CharField(
        forms.PasswordInput(
            attrs={
                'class': 'form-control', 
                'placeholder': '********'
            }), min_length=8)

    first_name = forms.CharField(
        forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Имя'
            }), help_text='First name')
    
    last_name = forms.CharField(
        forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Фамилия'
            }), help_text='Last name')
    
    gender = forms.CharField(
        forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Пол'
            }), help_text='Gender')
    
    age = forms.IntegerField(
        forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Возраст'
            }), help_text='Age')
    
    post = forms.CharField(
        forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Статус'
            }), help_text='Post')
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            'login', 
            'password', 
            'first_name', 
            'last_name', 
            'gender',
            'age',
            'post'
        )


