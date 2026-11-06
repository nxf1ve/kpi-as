from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('cabinet/admin/', views.cabinet_admin, name='cabinet-admin'),
    path('cabinet/manager/', views.cabinet_manager, name='cabinet-manager'),
    path('cabinet/employee/', views.cabinet_employee, name='cabinet-employee'),
]
