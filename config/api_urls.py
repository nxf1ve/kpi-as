"""Корневые маршруты REST API."""

from django.urls import include, path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    return Response(
        {
            'name': 'Расчет KPI',
            'endpoints': {
                'health': '/api/health/',
                'accounts': '/api/accounts/',
                'accounts_me': '/api/accounts/me/',
                'org': '/api/org/',
                'kpi': '/api/kpi/',
                'calculation': '/api/calculation/',
                'reports': '/api/reports/',
            },
        }
    )


@api_view(['GET'])
@permission_classes([AllowAny])
def health(request):
    return Response({'status': 'ok'})


urlpatterns = [
    path('', api_root, name='api-root'),
    path('health/', health, name='api-health'),
    path('accounts/', include('accounts.api_urls')),
    path('org/', include('org.api_urls')),
    path('kpi/', include('kpi.api_urls')),
    path('calculation/', include('calculation.api_urls')),
    path('reports/', include('reports.api_urls')),
]
