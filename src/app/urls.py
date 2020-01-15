from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('signup', views.CreateAccount.as_view(), name='signup'),
    path('generate_password', views.GeneratePassword.as_view(), name='generate_password'),
    path('manage_account', views.ManageAccount.as_view(), name='manage_account'),
    path('', include('user_sessions.urls', 'user_sessions')),
]