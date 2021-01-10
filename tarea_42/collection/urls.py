from django.contrib import admin
from django.urls import path
from collection import views

app_name = "collection"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
]
