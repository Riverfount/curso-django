from django.urls import path

from pypro.core import views

urlpatterns = [
    path('', views.home, name='home'),
]
