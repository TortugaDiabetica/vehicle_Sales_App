from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
import re


# Expresiones regulares para la validación y creación de contraseñas seguras:
def password_complexity_validator(value):
    if not re.search(r"\d", value):  # Al menos un número
        raise ValidationError("La contraseña debe contener al menos un número.")
    if not re.search(r"[A-Z]", value):  # Al menos una letra mayúscula
        raise ValidationError(
            "La contraseña debe contener al menos una letra mayúscula."
        )
    if not re.search(r"[\W_]", value):  # Al menos un carácter especial
        raise ValidationError(
            "La contraseña debe contener al menos un carácter especial."
        )
    if len(value) < 12:  # Longitud mínima
        raise ValidationError("La contraseña debe tener al menos 12 caracteres.")


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    # Validadores personalizados
    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        password_complexity_validator(password)  # Añadir la validación
        return password

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # Validar que el correo electrónico es único
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está en uso.")
        # Validación de formato de correo electrónico
        EmailValidator()(email)
        return email
