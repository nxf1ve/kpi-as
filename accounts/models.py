from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    """Роль пользователя системы (admin / manager / employee)."""

    class Code(models.TextChoices):
        ADMIN = 'admin', 'Администратор'
        MANAGER = 'manager', 'Руководитель'
        EMPLOYEE = 'employee', 'Сотрудник'

    name = models.CharField('Название', max_length=64)
    code = models.CharField(
        'Код',
        max_length=32,
        unique=True,
        choices=Code.choices,
    )

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
        ordering = ['id']

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    """Пользователь АС расчёта KPI (ER: User ↔ Role)."""

    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        related_name='users',
        verbose_name='Роль',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self) -> str:
        return self.username

    @property
    def role_code(self) -> str | None:
        if self.role_id is None:
            return None
        return self.role.code

    def has_role(self, *codes: str) -> bool:
        code = self.role_code
        return bool(code and code in codes)
