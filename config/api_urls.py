"""Корневые маршруты REST API (заготовки этапа 0)."""

from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request):
    return Response(
        {
            'name': 'Расчет KPI',
            'stage': 0,
            'endpoints': {
                'health': '/api/health/',
                'accounts': '/api/accounts/',
                'org': '/api/org/',
                'kpi': '/api/kpi/',
                'calculation': '/api/calculation/',
                'reports': '/api/reports/',
            },
        }
    )


@api_view(['GET'])
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
