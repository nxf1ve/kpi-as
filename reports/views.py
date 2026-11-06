from django.shortcuts import render

from accounts.permissions import role_required


@role_required('admin', 'manager', 'employee')
def stub(request):
    return render(
        request,
        'stub_module.html',
        {
            'page_title': 'Отчёты и аналитика',
            'module_hint': 'Индивидуальные и сводные отчёты, диаграммы и экспорт.',
        },
    )
