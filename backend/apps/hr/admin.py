from django.contrib import admin
from .models import Department, Designation, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "organization",
        "manager",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "organization__name",
    )

    list_filter = (
        "organization",
        "is_active",
    )

    ordering = (
        "organization",
        "name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "department",
        "level",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "department",
        "level",
        "is_active",
    )

    ordering = (
        "department",
        "level",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        "employee_id",
        "user",
        "organization",
        "department",
        "designation",
        "employment_status",
        "joining_date",
    )

    search_fields = (
        "employee_id",
        "user__first_name",
        "user__last_name",
        "user__email",
    )

    list_filter = (
        "organization",
        "department",
        "designation",
        "employment_status",
        "employment_type",
    )

    autocomplete_fields = (
        "user",
        "organization",
        "department",
        "designation",
        "manager",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "employee_id",
    )

    fieldsets = (

        (
            "System Information",
            {
                "fields": (
                    "employee_id",
                    "user",
                )
            },
        ),

        (
            "Organization Information",
            {
                "fields": (
                    "organization",
                    "department",
                    "designation",
                    "manager",
                )
            },
        ),

        (
            "Personal Information",
            {
                "fields": (
                    "gender",
                    "date_of_birth",
                    "profile_photo",
                )
            },
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "phone",
                    "alternate_phone",
                    "address",
                    "city",
                    "state",
                    "country",
                    "postal_code",
                )
            },
        ),

        (
            "Employment",
            {
                "fields": (
                    "joining_date",
                    "employment_type",
                    "employment_status",
                )
            },
        ),

        (
            "Salary",
            {
                "fields": (
                    "basic_salary",
                    "bank_name",
                    "account_number",
                    "ifsc_code",
                )
            },
        ),

        (
            "Government Information",
            {
                "fields": (
                    "pan_number",
                    "aadhaar_number",
                )
            },
        ),

        (
            "Emergency Contact",
            {
                "fields": (
                    "emergency_contact_name",
                    "emergency_contact_relationship",
                    "emergency_contact_phone",
                )
            },
        ),

        (
            "Audit Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
