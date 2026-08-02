from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PurchaseOrderViewSet,
    PurchaseOrderItemViewSet,
    GoodsReceiptViewSet,
)

router = DefaultRouter()

router.register(
    "purchase-orders",
    PurchaseOrderViewSet,
)

router.register(
    "purchase-items",
    PurchaseOrderItemViewSet,
)

router.register(
    "goods-receipts",
    GoodsReceiptViewSet,
)

urlpatterns = [
    path("", include(router.urls)),
]