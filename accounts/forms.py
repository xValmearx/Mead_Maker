from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)

from django import forms
from django.contrib.auth import get_user_model

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custome User Creaton Form"""

    class Meta:
        """This is the Meta class. it contains information"""

        # about how to get an instance of class created.
        # it is not common to se this, but Django dose for
        # certain things. Like this

        model = CustomUser
        fields = (
        "username", 
        "first_name", 
        "last_name", 
        "email", 
        "date_of_birth",
        )


class CustomUserChangeForm(UserChangeForm):
    """Custome User Change Form"""

    class Meta:
        """meta"""

        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
        )


class SignUpForm(forms.ModelForm):

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )

    password_confirm = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
        ]

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError(
                    "Passwords do not match."
                )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data["password"]
        )

        if commit:
            user.save()

        return user


class CustomLoginForm(AuthenticationForm):
    """Custom login form"""

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Enter your username",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Enter your password",
            }
        )
    )






    