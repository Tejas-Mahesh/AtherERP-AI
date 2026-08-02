from rest_framework.routers import DefaultRouter

from .views import (
    SupplierViewSet,
    SupplierContactViewSet,
    SupplierBankAccountViewSet,
    SupplierDocumentViewSet,
)

router = DefaultRouter()

router.register(
    "suppliers",
    SupplierViewSet,
)

router.register(
    "contacts",
    SupplierContactViewSet,
)

router.register(
    "bank-accounts",
    SupplierBankAccountViewSet,
)

router.register(
    "documents",
    SupplierDocumentViewSet,
)

urlpatterns = router.urls