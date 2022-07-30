from django import urls
from django.urls import path, include, re_path
from . import  views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('edit/<slug:slug>', views.edit, name="edit"),
    path('delete/<slug:slug>', views.delete, name="delete"),
    re_path(r'^(?P<path>.*)$',views.common, name="common"),
]