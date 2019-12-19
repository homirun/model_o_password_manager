from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, View, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
import string
import secrets
from . import forms


# def index(request):
#     return render(request, 'index.html')


class Index(LoginView):
    form_class = forms.LoginForm
    template_name = 'index.html'


class ManageAccount(TemplateView):
    template_name = 'manage_account.html'


class CreateAccount(CreateView):
    def post(self, request, *args, **kwargs):
        form = forms.UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'signup.html', {'form': form, })

    def get(self, request, *args, **kwargs):
        form = forms.UserCreateForm(request.POST)
        return render(request, 'signup.html', {'form': form, })


class GeneratePassword(CreateView):
    def post(self, request, *args, **kwargs):
        generated_password = self.generate()
        return render(request, 'generate_password.html', {'generated_password': generated_password, })

    def get(self, request, *args, **kwargs):
        return render(request, 'generate_password.html')

    @staticmethod
    def generate(size=12):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        # 記号を含める場合
        # chars += '%&$#()'

        return ''.join(secrets.choice(chars) for x in range(size))
