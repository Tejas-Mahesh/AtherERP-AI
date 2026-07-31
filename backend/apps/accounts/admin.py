from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserProfile, Role


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "email",
        "username",
        "organization",
        "role",
        "is_active",
        "is_verified",
        "is_staff",
    )

    search_fields = (
        "email",
        "username",
        "phone_number",
    )

    list_filter = (
        "organization",
        "role",
        "is_active",
        "is_verified",
        "is_staff",
    )

    ordering = (
        "email",
    )

    autocomplete_fields = (
        "organization",
        "role",
    )

    readonly_fields = (
        "last_login",
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Login Information",
            {
                "fields": (
                    "email",
                    "username",
                    "password",
                )
            },
        ),
        (
            "Organization",
            {
                "fields": (
                    "organization",
                    "role",
                )
            },
        ),
        (
            "Personal Information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                    "profile_picture",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Security",
            {
                "fields": (
                    "failed_login_attempts",
                    "account_locked_until",
                    "last_password_change",
                )
            },
        ),
        (
            "Audit",
            {
                "fields": (
                    "last_login",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "organization",
                    "role",
                ),
            },
        ),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "city",
        "country",
    )

    search_fields = (
        "user__email",
        "city",
    )

    list_filter = (
        "country",
        "state",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "organization",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "organization",
    )

    filter_horizontal = (
        "permissions",
    )

    autocomplete_fields = (
        "organization",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )