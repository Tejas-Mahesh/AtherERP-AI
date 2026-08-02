from django.contrib import admin

from .models import (
    Supplier,
    SupplierContact,
    SupplierBankAccount,
    SupplierDocument,
)
class SupplierContactInline(admin.TabularInline):
    model = SupplierContact
    extra = 1
class SupplierBankAccountInline(admin.TabularInline):
    model = SupplierBankAccount
    extra = 1
class SupplierDocumentInline(admin.TabularInline):
    model = SupplierDocument
    extra = 1
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = (
        "supplier_code",
        "name",
        "company_name",
        "contact_person",
        "phone",
        "email",
        "status",
    )

    list_filter = (
        "status",
        "organization",
        "country",
    )

    search_fields = (
        "supplier_code",
        "name",
        "company_name",
        "contact_person",
        "email",
        "phone",
        "gst_number",
        "pan_number",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [
        SupplierContactInline,
        SupplierBankAccountInline,
        SupplierDocumentInline,
    ]

    fieldsets = (

        (
            "Basic Information",
            {
                "fields": (
                    "organization",
                    "supplier_code",
                    "status",
                )
            },
        ),

        (
            "Company Details",
            {
                "fields": (
                    "name",
                    "company_name",
                    "contact_person",
                )
            },
        ),

        (
            "Contact Details",
            {
                "fields": (
                    "email",
                    "phone",
                    "mobile",
                    "website",
                )
            },
        ),

        (
            "Tax Information",
            {
                "fields": (
                    "gst_number",
                    "pan_number",
                )
            },
        ),

        (
            "Address",
            {
                "fields": (
                    "address",
                    "city",
                    "state",
                    "country",
                    "postal_code",
                )
            },
        ),

        (
            "Business",
            {
                "fields": (
                    "payment_terms",
                    "credit_limit",
                )
            },
        ),

        (
            "Notes",
            {
                "fields": (
                    "notes",
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
@admin.register(SupplierContact)
class SupplierContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "supplier",
        "designation",
        "department",
        "mobile",
        "is_primary",
    )

    search_fields = (
        "name",
        "supplier__name",
    )


@admin.register(SupplierBankAccount)
class SupplierBankAccountAdmin(admin.ModelAdmin):

    list_display = (
        "supplier",
        "bank_name",
        "account_holder_name",
        "account_number",
        "is_default",
    )

    search_fields = (
        "supplier__name",
        "bank_name",
    )


@admin.register(SupplierDocument)
class SupplierDocumentAdmin(admin.ModelAdmin):

    list_display = (
        "supplier",
        "document_name",
        "document_type",
        "is_verified",
        "expiry_date",
    )

    list_filter = (
        "document_type",
        "is_verified",
    )