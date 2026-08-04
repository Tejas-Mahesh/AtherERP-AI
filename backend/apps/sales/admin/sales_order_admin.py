from django.contrib import admin

from apps.sales.models import (
    SalesOrder,
    SalesOrderItem,
)


class SalesOrderItemInline(admin.TabularInline):
    """
    Inline items for Sales Order.
    """

    model = SalesOrderItem
    extra = 1

    autocomplete_fields = [
        "product",
    ]

    readonly_fields = [
        "delivered_quantity",
        "line_total",
    ]


@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    """
    Admin for Sales Order.
    """

    list_display = (
        "sales_order_number",
        "customer",
        "order_date",
        "expected_delivery_date",
        "status",
        "total_amount",
    )

    search_fields = (
        "sales_order_number",
        "customer__name",
    )

    list_filter = (
        "status",
        "order_date",
    )

    ordering = (
        "-order_date",
    )

    readonly_fields = (
        "subtotal",
        "tax_amount",
        "discount_amount",
        "total_amount",
        "approved_by",
        "approved_at",
        "created_at",
        "updated_at",
    )

    autocomplete_fields = [
        "customer",
        "quotation",
    ]

    inlines = [
        SalesOrderItemInline,
    ]