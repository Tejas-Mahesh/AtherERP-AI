from rest_framework.routers import DefaultRouter

from apps.sales.api.views.customer_view import CustomerViewSet
from apps.sales.api.views.quotation_view import QuotationViewSet
from apps.sales.api.views.sales_order_view import SalesOrderViewSet
from apps.sales.api.views.delivery_note_view import DeliveryNoteViewSet
from apps.sales.api.views.sales_invoice_view import SalesInvoiceViewSet
from apps.sales.api.views.customer_payment_view import (
    CustomerPaymentViewSet,
)
from apps.sales.api.views.sales_return_view import (
    SalesReturnViewSet,
)

router = DefaultRouter()

router.register(
    "customers",
    CustomerViewSet,
    basename="customer",
)

router.register(
    "quotations",
    QuotationViewSet,
    basename="quotation",
)

router.register(
    "sales-orders",
    SalesOrderViewSet,
    basename="sales-order",
)

router.register(
    "delivery-notes",
    DeliveryNoteViewSet,
    basename="delivery-note",
)

router.register(
    "sales-invoices",
    SalesInvoiceViewSet,
    basename="sales-invoice",
)

router.register(
    "customer-payments",
    CustomerPaymentViewSet,
    basename="customer-payment",
)

router.register(
    "sales-returns",
    SalesReturnViewSet,
    basename="sales-return",
)

urlpatterns = router.urls