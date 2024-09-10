from django.urls import path
from .views import UserRegistrationView,UserLoginView,UserLogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
]