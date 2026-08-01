from django.contrib import admin

from .models import (
    Category,
    Brand,
    Unit,
    Product,
    Warehouse,
    Stock,
    StockMovement,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "code",
        "organization",
        "parent",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "organization",
        "is_active",
    )

    autocomplete_fields = (
        "organization",
        "parent",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "code",
        "organization",
        "website",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "organization",
        "is_active",
    )

    autocomplete_fields = (
        "organization",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "symbol",
        "code",
        "organization",
        "is_active",
    )

    search_fields = (
        "name",
        "symbol",
        "code",
    )

    list_filter = (
        "organization",
        "is_active",
    )

    autocomplete_fields = (
        "organization",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "sku",
        "name",
        "category",
        "brand",
        "unit",
        "selling_price",
        "is_active",
    )

    search_fields = (
        "sku",
        "barcode",
        "name",
    )

    list_filter = (
        "organization",
        "category",
        "brand",
        "is_active",
    )

    autocomplete_fields = (
        "organization",
        "category",
        "brand",
        "unit",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "city",
        "manager",
        "phone_number",
        "is_active",
    )

    search_fields = (
        "code",
        "name",
        "city",
    )

    list_filter = (
        "organization",
        "city",
        "state",
        "is_active",
    )

    autocomplete_fields = (
        "organization",
        "manager",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "warehouse",
        "quantity",
        "reserved_quantity",
        "get_available_quantity",
        "get_inventory_value",
    )

    search_fields = (
        "product__name",
        "product__sku",
    )

    list_filter = (
        "warehouse",
    )

    autocomplete_fields = (
        "product",
        "warehouse",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "last_stock_update",
    )

    @admin.display(description="Available Qty")
    def get_available_quantity(self, obj):
        return obj.available_quantity

    @admin.display(description="Inventory Value")
    def get_inventory_value(self, obj):
        return obj.inventory_value


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "warehouse",
        "movement_type",
        "quantity",
        "reference",
        "created_at",
    )

    search_fields = (
        "product__name",
        "reference",
    )

    list_filter = (
        "movement_type",
        "warehouse",
    )

    autocomplete_fields = (
        "product",
        "warehouse",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )