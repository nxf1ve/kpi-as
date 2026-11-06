"""Проверки ролей для представлений и API."""

from functools import wraps

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from rest_framework.permissions import BasePermission


def role_required(*role_codes: str):
    """Доступ только для авторизованных пользователей с указанными ролями."""

    def decorator(view_func):
        @login_required
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            user = request.user
            if not user.is_active or not user.has_role(*role_codes):
                return render(request, '403.html', status=403)
            return view_func(request, *args, **kwargs)

        return _wrapped

    return decorator


def redirect_authenticated_user(view_func):
    """Если пользователь уже вошёл — сразу в кабинет своей роли."""

    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:cabinet')
        return view_func(request, *args, **kwargs)

    return _wrapped


class IsAuthenticatedAndActive(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.is_active)


class HasRole(BasePermission):
    """DRF: указать allowed_roles на view (список кодов ролей)."""

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated or not user.is_active:
            return False
        allowed = getattr(view, 'allowed_roles', None)
        if not allowed:
            return True
        return user.has_role(*allowed)
