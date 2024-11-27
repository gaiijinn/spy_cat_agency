from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import test


app_name = 'cats'

urlpatterns = [
    path('', test, name='test')
]