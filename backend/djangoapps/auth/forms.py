import logging

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.utils.translation import gettext_lazy as _

from backend.djangoapps.auth.validators import not_in_admin, min_username
from backend.models import JLPT_CHOICES

logger = logging.getLogger(__name__)


class RegistForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control", 
            'placeholder': _('Please enter your ID.')
        }),
        validators=[not_in_admin, min_username],
        error_messages={
            'unique': _("ID already exists."),
        }
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': "form-control", 
            'placeholder': _('Please enter your Email.')
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control", 
            'placeholder': _('Please enter your Password.')
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control", 
            'placeholder': _('Please enter your Password Check.')
        })
    )

    jlpt = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': "form-control custom-select"
        }), 
        choices=JLPT_CHOICES
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control", 
            'placeholder': _('Please enter your ID.')
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control", 
            'placeholder': _('Please enter your Password.')
        })
    )


class ResetForm(forms.Form):

    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': "form-control", 
            'placeholder': _('Please enter your Email.')
        })
    )


class ResetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control", 
            'placeholder': _('Please enter your Password.')
        })
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control", 
            'placeholder': _('Please enter your Password Check.')
        })
    )

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')