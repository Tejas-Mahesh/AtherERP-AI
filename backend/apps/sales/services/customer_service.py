from django.db import transaction

from apps.sales.models import Customer


class CustomerService:
    """
    Customer business logic.
    """

    @staticmethod
    def validate_customer(customer):
        """
        Validate customer before transactions.
        """

        if not customer.is_active:
            raise ValueError(
                "Customer is inactive."
            )

        return customer

    @staticmethod
    def validate_customer_code(customer_code):
        """
        Ensure customer code is unique.
        """

        exists = Customer.objects.filter(
            customer_code=customer_code
        ).exists()

        if exists:
            raise ValueError(
                "Customer code already exists."
            )

    @staticmethod
    @transaction.atomic
    def create_customer(**validated_data):
        """
        Create customer.
        """

        CustomerService.validate_customer_code(
            validated_data["customer_code"]
        )

        return Customer.objects.create(
            **validated_data
        )

    @staticmethod
    @transaction.atomic
    def activate_customer(customer):
        """
        Activate customer.
        """

        customer.is_active = True
        customer.save()

        return customer

    @staticmethod
    @transaction.atomic
    def deactivate_customer(customer):
        """
        Deactivate customer.
        """

        customer.is_active = False
        customer.save()

        return customer