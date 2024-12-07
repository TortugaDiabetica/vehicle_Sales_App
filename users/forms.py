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


# # Validación de RUT
# def rut_validation(rut):
#     # Elimina puntos y guión
#     rut = rut.replace(".", "").replace("-", "")

#     if len(rut) < 2:
#         raise ValidationError("El RUT ingresado no es válido.")

#     cuerpo = rut[:-1]
#     digito_verificador = rut[-1].upper()

#     try:
#         cuerpo = int(cuerpo)
#     except ValueError:
#         raise ValidationError("El RUT ingresado no es válido.")

#     # Cálculo del dígito verificador
#     suma = 0
#     multiplicador = 2

#     for digito in reversed(str(cuerpo)):
#         suma += int(digito) * multiplicador
#         multiplicador = 9 if multiplicador == 7 else multiplicador + 1

#     resto = suma % 11
#     dv_calculado = "K" if resto == 10 else str(11 - resto)

#     if dv_calculado != digito_verificador:
#         raise ValidationError("El RUT ingresado no es válido.")
