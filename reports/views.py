from django.shortcuts import render


def stub(request):
    return render(
        request,
        'stub_module.html',
        {
            'page_title': 'Отчёты и аналитика',
            'module_hint': 'Индивидуальные и сводные отчёты, диаграммы и экспорт.',
        },
    )
