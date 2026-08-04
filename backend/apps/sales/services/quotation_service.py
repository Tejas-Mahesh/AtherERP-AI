from django.db import transaction

from apps.sales.models import (
    Quotation,
    SalesOrder,
)


class QuotationService:
    """
    Quotation business logic.
    """

    @staticmethod
    def validate_quotation_number(number):
        """
        Ensure quotation number is unique.
        """

        exists = Quotation.objects.filter(
            quotation_number=number
        ).exists()

        if exists:
            raise ValueError(
                "Quotation number already exists."
            )

    @staticmethod
    @transaction.atomic
    def create_quotation(**validated_data):
        """
        Create a quotation.
        """

        QuotationService.validate_quotation_number(
            validated_data["quotation_number"]
        )

        return Quotation.objects.create(
            **validated_data
        )

    @staticmethod
    @transaction.atomic
    def calculate_totals(quotation):
        """
        Calculate quotation totals.
        """

        subtotal = 0
        tax = 0
        discount = 0

        for item in quotation.items.all():

            subtotal += (
                item.unit_price * item.quantity
            )

            tax += item.tax_amount
            discount += item.discount_amount

        quotation.subtotal = subtotal
        quotation.tax_amount = tax
        quotation.discount_amount = discount

        quotation.total_amount = (
            subtotal
            + tax
            - discount
        )

        quotation.save()

        return quotation

    @staticmethod
    @transaction.atomic
    def submit(quotation):
        """
        Submit quotation.
        """

        if quotation.status != "DRAFT":
            raise ValueError(
                "Only draft quotations can be submitted."
            )

        quotation.status = "SUBMITTED"
        quotation.save()

        return quotation

    @staticmethod
    @transaction.atomic
    def approve(quotation):
        """
        Approve quotation.
        """

        if quotation.status != "SUBMITTED":
            raise ValueError(
                "Only submitted quotations can be approved."
            )

        quotation.status = "APPROVED"
        quotation.save()

        return quotation

    @staticmethod
    @transaction.atomic
    def reject(quotation):
        """
        Reject quotation.
        """

        quotation.status = "REJECTED"
        quotation.save()

        return quotation

    @staticmethod
    @transaction.atomic
    def expire(quotation):
        """
        Expire quotation.
        """

        quotation.status = "EXPIRED"
        quotation.save()

        return quotation

    @staticmethod
    @transaction.atomic
    def convert_to_sales_order(
        quotation,
        sales_order_number,
    ):
        """
        Convert quotation into Sales Order.
        """

        if quotation.status != "APPROVED":
            raise ValueError(
                "Only approved quotations can be converted."
            )

        sales_order = SalesOrder.objects.create(
            customer=quotation.customer,
            quotation=quotation,
            sales_order_number=sales_order_number,
            order_date=quotation.quotation_date,
            expected_delivery_date=quotation.valid_until,
            subtotal=quotation.subtotal,
            tax_amount=quotation.tax_amount,
            discount_amount=quotation.discount_amount,
            total_amount=quotation.total_amount,
            remarks=quotation.remarks,
        )

        for item in quotation.items.all():

            sales_order.items.create(
                product=item.product,
                description=item.description,
                quantity=item.quantity,
                unit_price=item.unit_price,
                discount_amount=item.discount_amount,
                tax_amount=item.tax_amount,
                line_total=item.line_total,
            )

        quotation.status = "CONVERTED"
        quotation.save()

        return sales_order