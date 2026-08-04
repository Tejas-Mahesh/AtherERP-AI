from django.contrib import admin

from apps.sales.models import (
    Quotation,
    QuotationItem,
)


class QuotationItemInline(admin.TabularInline):
    """
    Inline items for Quotation.
    """

    model = QuotationItem
    extra = 1

    autocomplete_fields = [
        "product",
    ]


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    """
    Admin for Quotation.
    """

    list_display = (
        "quotation_number",
        "customer",
        "quotation_date",
        "valid_until",
        "status",
        "total_amount",
    )

    search_fields = (
        "quotation_number",
        "customer__name",
    )

    list_filter = (
        "status",
        "quotation_date",
    )

    ordering = (
        "-quotation_date",
    )

    readonly_fields = (
        "subtotal",
        "tax_amount",
        "discount_amount",
        "total_amount",
        "created_at",
        "updated_at",
    )

    autocomplete_fields = [
        "customer",
    ]

    inlines = [
        QuotationItemInline,
    ]