from rest_framework import serializers

from apps.sales.models import CustomerPayment


class CustomerPaymentSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for Customer Payment.
    """

    class Meta:
        model = CustomerPayment
        fields = "__all__"