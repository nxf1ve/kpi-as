from django.urls import path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from accounts.permissions import IsAuthenticatedAndActive


@api_view(['GET'])
@permission_classes([AllowAny])
def stub(request):
    return Response(
        {
            'app': 'accounts',
            'detail': 'Auth и роли активны. Войдите через /login/.',
            'endpoints': {
                'me': '/api/accounts/me/',
            },
        }
    )


@api_view(['GET'])
@permission_classes([IsAuthenticatedAndActive])
def me(request):
    user = request.user
    return Response(
        {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_active': user.is_active,
            'role': {
                'code': user.role_code,
                'name': user.role.name if user.role_id else None,
            },
        }
    )


urlpatterns = [
    path('', stub, name='api-accounts'),
    path('me/', me, name='api-accounts-me'),
]
