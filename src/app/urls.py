from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.CreateAccount.as_view(), name='signup'),
]