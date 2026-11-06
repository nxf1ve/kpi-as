from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_POST

from .forms import LoginForm, RegistrationForm
from .permissions import redirect_authenticated_user, role_required


def permission_denied(request, exception=None):
    return render(request, '403.html', status=403)


CABINET_CONFIG = {
    'admin': {
        'page_title': 'Кабинет администратора',
        'role_label': 'Администратор',
        'placeholders': [
            'Управление пользователями и ролями',
            'Настройка шкалы оценки',
            'Журнал аудита',
            'Сводные отчёты',
        ],
    },
    'manager': {
        'page_title': 'Кабинет руководителя',
        'role_label': 'Руководитель',
        'placeholders': [
            'Сотрудники и подразделения',
            'Справочник KPI и матрица',
            'Ввод фактов и расчёт',
            'Отчёты подразделения',
        ],
    },
    'employee': {
        'page_title': 'Кабинет сотрудника',
        'role_label': 'Сотрудник',
        'placeholders': [
            'Просмотр собственных KPI',
            'Результат расчёта (балл, категория)',
            'Личный отчёт и динамика',
        ],
    },
}


def _cabinet_url_for_user(user):
    code = user.role_code
    if code == 'admin':
        return 'accounts:cabinet-admin'
    if code == 'manager':
        return 'accounts:cabinet-manager'
    if code == 'employee':
        return 'accounts:cabinet-employee'
    return 'accounts:home'


def home(request):
    return render(
        request,
        'accounts/home.html',
        {
            'page_title': 'Расчет KPI',
        },
    )


@redirect_authenticated_user
@require_http_methods(['GET', 'POST'])
def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        if not user.role_id:
            messages.error(
                request,
                'У учётной записи не назначена роль. Обратитесь к администратору.',
            )
        else:
            login(request, user)
            messages.success(request, f'Вы вошли как {user.get_username()}.')
            next_url = request.GET.get('next') or request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect(_cabinet_url_for_user(user))

    return render(
        request,
        'accounts/login.html',
        {
            'page_title': 'Вход в систему',
            'form': form,
            'next': request.GET.get('next', ''),
        },
    )


@redirect_authenticated_user
@require_http_methods(['GET', 'POST'])
def register_view(request):
    form = RegistrationForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(
            request,
            'Регистрация выполнена. Вам назначена роль сотрудника.',
        )
        return redirect(_cabinet_url_for_user(user))

    return render(
        request,
        'accounts/register.html',
        {
            'page_title': 'Регистрация',
            'form': form,
        },
    )


@require_POST
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы.')
    return redirect('accounts:login')


@login_required
def cabinet(request):
    """Единая точка входа в кабинет текущей роли."""
    return redirect(_cabinet_url_for_user(request.user))


@role_required('admin')
def cabinet_admin(request):
    cfg = CABINET_CONFIG['admin']
    return render(
        request,
        'accounts/cabinet.html',
        {
            'page_title': cfg['page_title'],
            'role': 'admin',
            'role_label': cfg['role_label'],
            'placeholders': cfg['placeholders'],
        },
    )


@role_required('manager')
def cabinet_manager(request):
    cfg = CABINET_CONFIG['manager']
    return render(
        request,
        'accounts/cabinet.html',
        {
            'page_title': cfg['page_title'],
            'role': 'manager',
            'role_label': cfg['role_label'],
            'placeholders': cfg['placeholders'],
        },
    )


@role_required('employee')
def cabinet_employee(request):
    cfg = CABINET_CONFIG['employee']
    return render(
        request,
        'accounts/cabinet.html',
        {
            'page_title': cfg['page_title'],
            'role': 'employee',
            'role_label': cfg['role_label'],
            'placeholders': cfg['placeholders'],
        },
    )
