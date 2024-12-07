from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from django.contrib.auth import logout


User = get_user_model()


class CustomLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("common:home")


class RegisterView(FormView):
    template_name = "sign_up.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("common:home")

    def form_valid(self, form):
        user = form.save()
        if user:
            # Añadir el usuario al grupo "Cliente"
            cliente_group, created = Group.objects.get_or_create(name="Cliente")
            user.groups.add(cliente_group)
            login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("common:home")
        return super().get(*args, **kwargs)


def custom_logout_view(request):
    logout(request)
    return redirect("users:login")
