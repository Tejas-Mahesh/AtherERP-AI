from django.contrib import admin

from apps.sales.models import (
    SalesReturn,
    SalesReturnItem,
)


class SalesReturnItemInline(admin.TabularInline):
    """
    Inline items for Sales Return.
    """

    model = SalesReturnItem
    extra = 1

    autocomplete_fields = [
        "product",
        "sales_invoice_item",
        "location",
    ]

    readonly_fields = (
        "refund_amount",
    )


@admin.register(SalesReturn)
class SalesReturnAdmin(admin.ModelAdmin):
    """
    Admin for Sales Return.
    """

    list_display = (
        "return_number",
        "customer",
        "sales_invoice",
        "return_date",
        "status",
        "total_amount",
    )

    search_fields = (
        "return_number",
        "customer__name",
        "sales_invoice__invoice_number",
    )

    list_filter = (
        "status",
        "return_date",
    )

    ordering = (
        "-return_date",
    )

    readonly_fields = (
        "total_amount",
        "created_at",
        "updated_at",
    )

    autocomplete_fields = [
        "customer",
        "sales_invoice",
        "received_by",
        "approved_by",
    ]

    inlines = [
        SalesReturnItemInline,
    ]