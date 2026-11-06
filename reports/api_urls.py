from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def stub(request):
    return Response({'app': 'reports', 'detail': 'Модуль отчётов.'})


urlpatterns = [
    path('', stub, name='api-reports'),
]
