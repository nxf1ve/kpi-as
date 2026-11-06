from django.urls import path

from . import views

app_name = 'kpi'

urlpatterns = [
    path('', views.stub, name='index'),
]
