from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView
from users.forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('http://127.0.0.1:8000/api/v1/drf-auth/login/')
    template_name = 'new_signup.html'
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_group = Group.objects.get(name=form.cleaned_data['groups'])
            user.groups.add(user_group)
            
            return redirect('http://127.0.0.1:8000/api/v1/drf-auth/login/')
        else:
            return render(request, self.template_name, {'form' : form})
        