from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, View
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from . import forms


def index(request):
    return render(request, 'index.html')


# def signup(request):
#     return render(request, 'signup.html')


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
