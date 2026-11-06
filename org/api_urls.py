from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def stub(request):
    return Response({'app': 'org', 'stage': 0, 'detail': 'Заготовка. Оргструктура — этап 2.'})


urlpatterns = [
    path('', stub, name='api-org'),
]
