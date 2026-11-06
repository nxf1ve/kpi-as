from django.shortcuts import render


def stub(request):
    return render(
        request,
        'stub_module.html',
        {
            'page_title': 'Показатели KPI',
            'module_hint': 'Справочник показателей, матрицы, оценочные периоды и шкала оценки.',
        },
    )
