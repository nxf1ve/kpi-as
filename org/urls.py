from django.urls import path

from . import views

app_name = 'org'

urlpatterns = [
    path('', views.stub, name='index'),
]
