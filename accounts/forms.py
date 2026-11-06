from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password

from .models import Role, User


class LoginForm(AuthenticationForm):
    """Форма входа в систему."""

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'username',
                'placeholder': 'Логин',
                'autofocus': True,
            }
        ),
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Пароль',
            }
        ),
    )

    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': 'Неверный логин или пароль.',
        'inactive': 'Учётная запись заблокирована.',
    }


class RegistrationForm(forms.ModelForm):
    """Простая регистрация: логин, пароль, повтор пароля."""

    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Пароль',
            }
        ),
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Повтор пароля',
            }
        ),
    )

    class Meta:
        model = User
        fields = ('username',)
        labels = {'username': 'Логин'}
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'autocomplete': 'username',
                    'placeholder': 'Логин',
                    'autofocus': True,
                }
            ),
        }

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Пользователь с таким логином уже существует.')
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            validate_password(password1)
        return password1

    def clean(self):
        cleaned = super().clean()
        password1 = cleaned.get('password1')
        password2 = cleaned.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Пароли не совпадают.')
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        role, _ = Role.objects.get_or_create(
            code=Role.Code.EMPLOYEE,
            defaults={'name': 'Сотрудник'},
        )
        user.role = role
        user.is_active = True
        if commit:
            user.save()
        return user
