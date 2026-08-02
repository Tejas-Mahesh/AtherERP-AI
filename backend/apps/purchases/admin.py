from django.contrib import admin

from .models import (
    PurchaseOrder,
    PurchaseOrderItem,
    GoodsReceipt,
)


class PurchaseOrderItemInline(admin.TabularInline):
    model = PurchaseOrderItem
    extra = 1

    fields = (
        "product",
        "quantity",
        "unit_price",
        "discount_amount",
        "tax_amount",
        "line_total",
        "received_quantity",
    )

    readonly_fields = (
        "received_quantity",
    )


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):

    list_display = (
        "purchase_number",
        "supplier",
        "organization",
        "status",
        "order_date",
        "total_amount",
    )

    search_fields = (
        "purchase_number",
        "supplier__name",
    )

    list_filter = (
        "status",
        "order_date",
    )

    ordering = (
        "-order_date",
    )

    date_hierarchy = "order_date"

    readonly_fields = (
        "approved_by",
        "approved_at",
    )

    inlines = [
        PurchaseOrderItemInline,
    ]


@admin.register(GoodsReceipt)
class GoodsReceiptAdmin(admin.ModelAdmin):

    list_display = (
        "receipt_number",
        "purchase_order",
        "warehouse",
        "receipt_date",
        "received_by",
    )

    search_fields = (
        "receipt_number",
        "purchase_order__purchase_number",
    )

    list_filter = (
        "receipt_date",
        "warehouse",
    )

    ordering = (
        "-receipt_date",
    )

    date_hierarchy = "receipt_date"