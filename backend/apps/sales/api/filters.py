import django_filters

from apps.sales.models import (
    Customer,
    Quotation,
    SalesOrder,
    DeliveryNote,
    SalesInvoice,
    CustomerPayment,
    SalesReturn,
)


class CustomerFilter(
    django_filters.FilterSet,
):

    class Meta:
        model = Customer
        fields = {
            "customer_type": ["exact"],
            "is_active": ["exact"],
            "city": ["exact", "icontains"],
            "state": ["exact", "icontains"],
        }


class QuotationFilter(
    django_filters.FilterSet,
):

    class Meta:
        model = Quotation
        fields = {
            "status": ["exact"],
            "customer": ["exact"],
            "quotation_date": [
                "exact",
                "gte",
                "lte",
            ],
            "valid_until": [
                "exact",
                "gte",
                "lte",
            ],
        }


class SalesOrderFilter(
    django_filters.FilterSet,
):

    class Meta:
        model = SalesOrder
        fields = {
            "status": ["exact"],
            "customer": ["exact"],
            "order_date": [
                "exact",
                "gte",
                "lte",
            ],
            "expected_delivery_date": [
                "exact",
                "gte",
                "lte",
            ],
        }


class DeliveryNoteFilter(
    django_filters.FilterSet,
):

    class Meta:
        model = DeliveryNote
        fields = {
            "status": ["exact"],
            "warehouse": ["exact"],
            "delivery_date": [
                "exact",
                "gte",
                "lte",
            ],
        }


class SalesInvoiceFilter(
    django_filters.FilterSet,
):

    class Meta:
        model = SalesInvoice
        fields = {
            "status": ["exact"],
            "customer": ["exact"],
            "invoice_date": [
                "exact",
                "gte",
                "lte",
            ],
        }


class CustomerPaymentFilter(
    django_filters.FilterSet,
):

    class Meta:
        model = CustomerPayment
        fields = {
            "status": ["exact"],
            "payment_method": ["exact"],
            "customer": ["exact"],
            "payment_date": [
                "exact",
                "gte",
                "lte",
            ],
        }


class SalesReturnFilter(
    django_filters.FilterSet,
):

    class Meta:
        model = SalesReturn
        fields = {
            "status": ["exact"],
            "customer": ["exact"],
            "return_date": [
                "exact",
                "gte",
                "lte",
            ],
        }