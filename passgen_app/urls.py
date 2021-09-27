from django.contrib import admin
from django.urls import path

from passgen_app import views
# user defined url file
urlpatterns = [
    path('app/', views.pass_gen, name='pass_gen'),
]