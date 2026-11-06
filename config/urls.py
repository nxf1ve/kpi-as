from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('org/', include('org.urls')),
    path('kpi/', include('kpi.urls')),
    path('calculation/', include('calculation.urls')),
    path('reports/', include('reports.urls')),
    path('api/', include('config.api_urls')),
]

handler403 = 'accounts.views.permission_denied'
