from django.shortcuts import render


def stub(request):
    return render(
        request,
        'stub_module.html',
        {
            'page_title': 'Расчёт показателей',
            'module_hint': 'Ввод фактических значений и расчёт интегрального показателя.',
        },
    )
