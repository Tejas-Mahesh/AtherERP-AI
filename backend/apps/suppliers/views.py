from rest_framework import viewsets

from .models import (
    Supplier,
    SupplierContact,
    SupplierBankAccount,
    SupplierDocument,
)

from .serializers import (
    SupplierSerializer,
    SupplierContactSerializer,
    SupplierBankAccountSerializer,
    SupplierDocumentSerializer,
)
class SupplierViewSet(viewsets.ModelViewSet):

    queryset = Supplier.objects.all()

    serializer_class = SupplierSerializer
class SupplierContactViewSet(viewsets.ModelViewSet):

    queryset = SupplierContact.objects.all()

    serializer_class = SupplierContactSerializer
class SupplierBankAccountViewSet(viewsets.ModelViewSet):

    queryset = SupplierBankAccount.objects.all()

    serializer_class = SupplierBankAccountSerializer
class SupplierDocumentViewSet(viewsets.ModelViewSet):

    queryset = SupplierDocument.objects.all()

    serializer_class = SupplierDocumentSerializer