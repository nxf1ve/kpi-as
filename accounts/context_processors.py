"""Контекст шаблонов: роль и пункты навигации по правам."""


NAV_BY_ROLE = {
    'admin': [
        {'label': 'Кабинет', 'url_name': 'accounts:cabinet-admin'},
        {'label': 'Отчёты', 'url_name': 'reports:index'},
    ],
    'manager': [
        {'label': 'Кабинет', 'url_name': 'accounts:cabinet-manager'},
        {'label': 'Оргструктура', 'url_name': 'org:index'},
        {'label': 'KPI', 'url_name': 'kpi:index'},
        {'label': 'Расчёт', 'url_name': 'calculation:index'},
        {'label': 'Отчёты', 'url_name': 'reports:index'},
    ],
    'employee': [
        {'label': 'Кабинет', 'url_name': 'accounts:cabinet-employee'},
        {'label': 'Отчёты', 'url_name': 'reports:index'},
    ],
}


def auth_nav(request):
    user = getattr(request, 'user', None)
    nav_items = []
    role_code = None
    role_label = None

    if user is not None and user.is_authenticated and user.is_active:
        role_code = user.role_code
        if role_code:
            role_label = user.role.name if user.role_id else None
            nav_items = NAV_BY_ROLE.get(role_code, [])

    return {
        'nav_items': nav_items,
        'user_role_code': role_code,
        'user_role_label': role_label,
    }
