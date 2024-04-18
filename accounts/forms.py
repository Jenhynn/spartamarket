from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.urls import reverse


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            "email",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.fields.get("password"):
            password_help_text = (
                "비밀번호 변경은 " '<a href="{}">여기를 눌러주세요</a>.'
            ).format(f"{reverse('accounts:change_password')}") # reverse: url name으로부터 url을 찾아가는 기능
            self.fields["password"].help_text = password_help_text