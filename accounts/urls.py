from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('cabinet/admin/', views.cabinet_admin, name='cabinet-admin'),
    path('cabinet/manager/', views.cabinet_manager, name='cabinet-manager'),
    path('cabinet/employee/', views.cabinet_employee, name='cabinet-employee'),
]
