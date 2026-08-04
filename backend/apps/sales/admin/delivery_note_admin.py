from django.contrib import admin

from apps.sales.models import (
    DeliveryNote,
    DeliveryNoteItem,
)


class DeliveryNoteItemInline(admin.TabularInline):
    """
    Inline items for Delivery Note.
    """

    model = DeliveryNoteItem
    extra = 1

    autocomplete_fields = [
        "product",
        "sales_order_item",
    ]

    readonly_fields = [
        "quantity",
    ]


@admin.register(DeliveryNote)
class DeliveryNoteAdmin(admin.ModelAdmin):
    """
    Admin for Delivery Note.
    """

    list_display = (
        "delivery_number",
        "sales_order",
        "warehouse",
        "delivery_date",
        "status",
    )

    search_fields = (
        "delivery_number",
        "sales_order__sales_order_number",
        "sales_order__customer__name",
    )

    list_filter = (
        "status",
        "delivery_date",
        "warehouse",
    )

    ordering = (
        "-delivery_date",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    autocomplete_fields = [
        "sales_order",
        "warehouse",
        "delivered_by",
    ]

    inlines = [
        DeliveryNoteItemInline,
    ]