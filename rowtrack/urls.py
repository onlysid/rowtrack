from django.contrib import admin
from django.urls import include, path

from rowtrack import consumers
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.rowMachine, name='rowMachine'),
]