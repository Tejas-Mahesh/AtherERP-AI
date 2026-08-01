from django.db import transaction

from .models import (
    Product,
    Stock,
    StockMovement,
)


class ProductService:
    """
    Product business logic.
    """

    @staticmethod
    @transaction.atomic
    def create_product(**validated_data):
        return Product.objects.create(**validated_data)

    @staticmethod
    @transaction.atomic
    def update_product(instance, **validated_data):

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()

        return instance


class StockService:
    """
    Stock business logic.
    """

    @staticmethod
    @transaction.atomic
    def receive_stock(
        stock,
        quantity,
        reference="",
        remarks="",
    ):

        stock.quantity += quantity
        stock.save()

        StockMovement.objects.create(
            product=stock.product,
            warehouse=stock.warehouse,
            movement_type="IN",
            quantity=quantity,
            reference=reference,
            remarks=remarks,
        )

        return stock

    @staticmethod
    @transaction.atomic
    def issue_stock(
        stock,
        quantity,
        reference="",
        remarks="",
    ):

        if quantity > stock.available_quantity:
            raise ValueError(
                "Insufficient stock available."
            )

        stock.quantity -= quantity
        stock.save()

        StockMovement.objects.create(
            product=stock.product,
            warehouse=stock.warehouse,
            movement_type="OUT",
            quantity=quantity,
            reference=reference,
            remarks=remarks,
        )

        return stock

    @staticmethod
    @transaction.atomic
    def adjust_stock(
        stock,
        new_quantity,
        reference="",
        remarks="",
    ):

        difference = abs(stock.quantity - new_quantity)

        stock.quantity = new_quantity
        stock.save()

        StockMovement.objects.create(
            product=stock.product,
            warehouse=stock.warehouse,
            movement_type="ADJUSTMENT",
            quantity=difference,
            reference=reference,
            remarks=remarks,
        )

        return stock