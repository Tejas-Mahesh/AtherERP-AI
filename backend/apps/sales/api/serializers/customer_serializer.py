from rest_framework import serializers

from apps.sales.models import (
    Customer,
    CustomerAddress,
    CustomerContact,
)


class CustomerAddressSerializer(
    serializers.ModelSerializer,
):

    class Meta:
        model = CustomerAddress
        fields = "__all__"


class CustomerContactSerializer(
    serializers.ModelSerializer,
):

    class Meta:
        model = CustomerContact
        fields = "__all__"


class CustomerSerializer(
    serializers.ModelSerializer,
):

    addresses = CustomerAddressSerializer(
        many=True,
        read_only=True,
    )

    contacts = CustomerContactSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Customer
        fields = "__all__"