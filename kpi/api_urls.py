from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def stub(request):
    return Response(
        {
            'app': 'kpi',
            'stage': 0,
            'detail': 'Заготовка. Конфигурация KPI — этап 3; расчёт POST /api/kpi/calculate — этап 4.',
        }
    )


urlpatterns = [
    path('', stub, name='api-kpi'),
]
