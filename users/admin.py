from .models import User, UserGroup
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "first_name", "last_name", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("username", "email", "first_name", "last_name", "password", )}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff")


class UserGroupAdmin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(UserGroup, UserGroupAdmin)