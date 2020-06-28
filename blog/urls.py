from django.contrib import admin
from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('blog/', views.blog, name='blog'),
]
