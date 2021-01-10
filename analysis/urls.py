from django.urls import path
from . import views

urlpatterns = [
    path('', views.datainputform, name='datainputform'),
]