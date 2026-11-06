from django.core.management.base import BaseCommand
from django.db import transaction

from accounts.models import Role, User


DEMO_ROLES = (
    (Role.Code.ADMIN, 'Администратор'),
    (Role.Code.MANAGER, 'Руководитель'),
    (Role.Code.EMPLOYEE, 'Сотрудник'),
)

DEMO_USERS = (
    {
        'username': 'admin',
        'password': 'admin123',
        'email': 'admin@kpi.local',
        'first_name': 'Анна',
        'last_name': 'Админова',
        'role_code': Role.Code.ADMIN,
        'is_staff': True,
        'is_superuser': True,
    },
    {
        'username': 'manager',
        'password': 'manager123',
        'email': 'manager@kpi.local',
        'first_name': 'Михаил',
        'last_name': 'Руководов',
        'role_code': Role.Code.MANAGER,
        'is_staff': False,
        'is_superuser': False,
    },
    {
        'username': 'employee',
        'password': 'employee123',
        'email': 'employee@kpi.local',
        'first_name': 'Елена',
        'last_name': 'Сотрудникова',
        'role_code': Role.Code.EMPLOYEE,
        'is_staff': False,
        'is_superuser': False,
    },
)


class Command(BaseCommand):
    help = 'Создаёт роли и демо-пользователей (admin / manager / employee).'

    @transaction.atomic
    def handle(self, *args, **options):
        roles = {}
        for code, name in DEMO_ROLES:
            role, created = Role.objects.update_or_create(
                code=code,
                defaults={'name': name},
            )
            roles[code] = role
            action = 'создана' if created else 'обновлена'
            self.stdout.write(f'Роль {code}: {action}')

        for spec in DEMO_USERS:
            role = roles[spec['role_code']]
            user, created = User.objects.get_or_create(
                username=spec['username'],
                defaults={
                    'email': spec['email'],
                    'first_name': spec['first_name'],
                    'last_name': spec['last_name'],
                    'role': role,
                    'is_staff': spec['is_staff'],
                    'is_superuser': spec['is_superuser'],
                    'is_active': True,
                },
            )
            if created:
                user.set_password(spec['password'])
                user.save()
                self.stdout.write(self.style.SUCCESS(
                    f"Пользователь {spec['username']} создан "
                    f"(пароль: {spec['password']})"
                ))
            else:
                user.email = spec['email']
                user.first_name = spec['first_name']
                user.last_name = spec['last_name']
                user.role = role
                user.is_staff = spec['is_staff']
                user.is_superuser = spec['is_superuser']
                user.is_active = True
                user.set_password(spec['password'])
                user.save()
                self.stdout.write(
                    f"Пользователь {spec['username']} обновлён "
                    f"(пароль сброшен: {spec['password']})"
                )

        self.stdout.write(self.style.SUCCESS('Демо-доступ готов.'))
