from django.contrib import admin

from apps.sales.models import (
    SalesInvoice,
    SalesInvoiceItem,
)


class SalesInvoiceItemInline(admin.TabularInline):
    """
    Inline items for Sales Invoice.
    """

    model = SalesInvoiceItem
    extra = 1

    autocomplete_fields = [
        "product",
        "sales_order_item",
    ]

    readonly_fields = (
        "line_total",
    )


@admin.register(SalesInvoice)
class SalesInvoiceAdmin(admin.ModelAdmin):
    """
    Admin for Sales Invoice.
    """

    list_display = (
        "invoice_number",
        "customer",
        "invoice_date",
        "status",
        "total_amount",
        "paid_amount",
        "balance_amount",
    )

    search_fields = (
        "invoice_number",
        "customer__name",
        "sales_order__sales_order_number",
    )

    list_filter = (
        "status",
        "invoice_date",
    )

    ordering = (
        "-invoice_date",
    )

    readonly_fields = (
        "subtotal",
        "tax_amount",
        "discount_amount",
        "total_amount",
        "paid_amount",
        "balance_amount",
        "created_at",
        "updated_at",
    )

    autocomplete_fields = [
        "customer",
        "sales_order",
    ]

    inlines = [
        SalesInvoiceItemInline,
    ]