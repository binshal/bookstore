from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views



urlpatterns = [

    path('register/', views.UserRegistration, name='register'),
    path('', views.loginPage, name='login'),
    path('logout/', views.logout_view, name='logout')


    # path('register/', views.register, name='register'),
    # path('login/', views.loginUser, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('home/', views.homepage, name='home'),
]