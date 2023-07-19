from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
	first_name = forms.CharField(
		widget = forms.TextInput(
		    attrs={
			    'class':'form-control',
			    'placeholder':'Имя'
            }
	    )
	)
	
	last_name = forms.CharField(
		widget = forms.TextInput(
		    attrs={
			    'class':'form-control',
			    'placeholder':'Фамилия'
            }
	    )
	)
	
	gender = forms.CharField(
		widget = forms.TextInput(
		    attrs={
			    'class':'form-control',
			    'placeholder':'Пол'
            }
	    )
	)
	
	age = forms.IntegerField(
		widget = forms.TextInput(
		    attrs={
			    'class':'form-control',
			    'placeholder':'Возраст'
            }
	    )
	)
	
	post = forms.CharField(
		widget = forms.TextInput(
		    attrs={
			    'class':'form-control',
			    'placeholder':'Статус'
            }
	    )
	)

	class Meta():
		model = User
		fields = (
			'username',  
            'first_name', 
            'last_name', 
            'gender',
            'age',
            'post',
            'password1',
            'password2'
	    )


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['gender'].widget.attrs['class'] = 'form-control'
		self.fields['age'].widget.attrs['class'] = 'form-control'
		self.fields['post'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		
		












""" class SignUpForm(UserCreationForm):
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
        ) """

