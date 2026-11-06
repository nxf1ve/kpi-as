from django.shortcuts import render


def stub(request):
    return render(
        request,
        'stub_module.html',
        {
            'page_title': 'Оргструктура',
            'module_hint': 'Ведение подразделений, должностей и карточек сотрудников.',
        },
    )
