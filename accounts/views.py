from django.shortcuts import render


def home(request):
    return render(
        request,
        'accounts/home.html',
        {
            'page_title': 'Расчет KPI',
        },
    )


def cabinet_admin(request):
    return render(
        request,
        'accounts/cabinet.html',
        {
            'page_title': 'Кабинет администратора',
            'role': 'admin',
            'role_label': 'Администратор',
            'placeholders': [
                'Управление пользователями и ролями',
                'Настройка шкалы оценки',
                'Журнал аудита',
                'Сводные отчёты',
            ],
        },
    )


def cabinet_manager(request):
    return render(
        request,
        'accounts/cabinet.html',
        {
            'page_title': 'Кабинет руководителя',
            'role': 'manager',
            'role_label': 'Руководитель',
            'placeholders': [
                'Сотрудники и подразделения',
                'Справочник KPI и матрица',
                'Ввод фактов и расчёт',
                'Отчёты подразделения',
            ],
        },
    )


def cabinet_employee(request):
    return render(
        request,
        'accounts/cabinet.html',
        {
            'page_title': 'Кабинет сотрудника',
            'role': 'employee',
            'role_label': 'Сотрудник',
            'placeholders': [
                'Просмотр собственных KPI',
                'Результат расчёта (балл, категория)',
                'Личный отчёт и динамика',
            ],
        },
    )
