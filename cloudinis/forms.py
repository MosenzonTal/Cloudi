from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CloudiniUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CloudiniUser
        fields = ('username', 'email',)

        def save(self, commit=True):
            user = super(CustomUserCreationForm, self).save(commit=False)
            user.is_active = None
            if commit:
                user.save()
            return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CloudiniUser
        fields = ('username', 'email',)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CloudiniUser
        fields = ['username', 'email','access_key', 'secret_key','session_token']

