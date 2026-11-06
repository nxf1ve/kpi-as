from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def stub(request):
    return Response({'app': 'kpi', 'detail': 'Модуль показателей KPI.'})


urlpatterns = [
    path('', stub, name='api-kpi'),
]
