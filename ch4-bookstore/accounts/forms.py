from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserCreationForm(UserCreationForm):
    class Meta:
        models = get_user_model()
        fields = (
            'email',
            'username',
        )


class UserChangeForm(UserChangeForm):
    class Meta:
        models = get_user_model()
        fields = (
            'email',
            'username',
        )
