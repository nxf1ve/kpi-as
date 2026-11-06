from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def stub(request):
    return Response({'app': 'accounts', 'stage': 0, 'detail': 'Заготовка. Auth и роли — этап 1.'})


urlpatterns = [
    path('', stub, name='api-accounts'),
]
