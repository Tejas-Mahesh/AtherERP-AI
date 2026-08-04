from django.contrib import admin

from apps.sales.models import CustomerPayment


@admin.register(CustomerPayment)
class CustomerPaymentAdmin(admin.ModelAdmin):
    """
    Admin for Customer Payment.
    """

    list_display = (
        "payment_number",
        "customer",
        "sales_invoice",
        "payment_date",
        "payment_method",
        "amount",
        "status",
    )

    search_fields = (
        "payment_number",
        "customer__name",
        "sales_invoice__invoice_number",
        "reference_number",
    )

    list_filter = (
        "status",
        "payment_method",
        "payment_date",
    )

    ordering = (
        "-payment_date",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    autocomplete_fields = [
        "customer",
        "sales_invoice",
        "received_by",
    ]