from django.contrib import admin

from apps.sales.models import (
    Customer,
    CustomerAddress,
    CustomerContact,
)


class CustomerAddressInline(admin.TabularInline):
    model = CustomerAddress
    extra = 0


class CustomerContactInline(admin.TabularInline):
    model = CustomerContact
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        "customer_code",
        "name",
        "email",
        "phone_number",
        "customer_type",
        "credit_limit",
        "is_active",
    )

    search_fields = (
        "customer_code",
        "name",
        "email",
        "phone_number",
    )

    list_filter = (
        "customer_type",
        "is_active",
    )

    ordering = (
        "customer_code",
    )

    inlines = [
        CustomerAddressInline,
        CustomerContactInline,
    ]