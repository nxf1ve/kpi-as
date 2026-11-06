from django.shortcuts import render

from accounts.permissions import role_required


@role_required('manager')
def stub(request):
    return render(
        request,
        'stub_module.html',
        {
            'page_title': 'Оргструктура',
            'module_hint': 'Ведение подразделений, должностей и карточек сотрудников.',
        },
    )
