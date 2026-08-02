from rest_framework import serializers

from .models import (
    Supplier,
    SupplierContact,
    SupplierBankAccount,
    SupplierDocument,
)
class SupplierContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupplierContact
        fields = "__all__"
class SupplierBankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupplierBankAccount
        fields = "__all__"
class SupplierDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupplierDocument
        fields = "__all__"
class SupplierSerializer(serializers.ModelSerializer):

    contacts = SupplierContactSerializer(
        many=True,
        read_only=True,
    )

    bank_accounts = SupplierBankAccountSerializer(
        many=True,
        read_only=True,
    )

    documents = SupplierDocumentSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Supplier
        fields = "__all__"