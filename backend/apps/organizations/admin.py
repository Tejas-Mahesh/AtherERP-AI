from django.contrib import admin

from .models import Organization, Branch, Location


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "legal_name",
        "email",
        "phone",
        "is_active",
    )

    search_fields = (
        "name",
        "legal_name",
        "email",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Organization Information",
            {
                "fields": (
                    "name",
                    "legal_name",
                )
            },
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "website",
                )
            },
        ),

        (
            "Address",
            {
                "fields": (
                    "address",
                )
            },
        ),

        (
            "Audit",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "code",
        "organization",
        "city",
        "state",
        "is_head_office",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "city",
    )

    list_filter = (
        "organization",
        "state",
        "is_head_office",
        "is_active",
    )

    autocomplete_fields = (
        "organization",
    )

    ordering = (
        "organization",
        "name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "branch",
        "location_type",
        "city",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "city",
    )

    list_filter = (
        "branch",
        "location_type",
        "is_active",
    )

    autocomplete_fields = (
        "branch",
    )

    ordering = (
        "branch",
        "name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )