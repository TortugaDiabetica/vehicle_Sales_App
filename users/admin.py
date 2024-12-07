from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.db.models import Q


class CustomUserAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Staff solo ve usuarios del grupo Cliente
        cliente_group = Group.objects.get(name="Cliente")
        return qs.filter(groups=cliente_group)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            if obj:
                # Deshabilitar campos sensibles para staff
                disabled_fields = [
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "groups",
                ]
                for field in disabled_fields:
                    if field in form.base_fields:
                        form.base_fields[field].disabled = True
        return form

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        if request.user.is_superuser:
            return True
        # Staff solo puede modificar usuarios del grupo Cliente
        return obj.groups.filter(name="Cliente").exists()

    def has_delete_permission(self, request, obj=None):
        if not obj:
            return True
        if request.user.is_superuser:
            return True
        # Staff solo puede eliminar usuarios del grupo Cliente
        return obj.groups.filter(name="Cliente").exists()

    def has_add_permission(self, request):
        # Staff puede añadir usuarios, pero se asignarán automáticamente al grupo Cliente
        return True

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            # Si es staff, asegurar que el nuevo usuario sea Cliente
            super().save_model(request, obj, form, change)
            cliente_group = Group.objects.get(name="Cliente")
            obj.groups.add(cliente_group)
            obj.is_staff = False
            obj.is_superuser = False
            obj.save()
        else:
            super().save_model(request, obj, form, change)


# Registrar el admin personalizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
