from django.db import transaction
from django.utils import timezone

from .models import PurchaseOrder

from django.db import transaction

from apps.inventory.models import (
    Stock,
    StockMovement,
)

from .models import (
    PurchaseOrder,
    GoodsReceipt,
)
class PurchaseOrderService:
    """
    Purchase Order business logic.
    """

    @staticmethod
    @transaction.atomic
    def submit(po):

        if po.status != "DRAFT":
            raise ValueError(
                "Only draft purchase orders can be submitted."
            )

        po.status = "SUBMITTED"
        po.save()

        return po

    @staticmethod
    @transaction.atomic
    def approve(po, approved_by):

        if po.status != "SUBMITTED":
            raise ValueError(
                "Only submitted purchase orders can be approved."
            )

        po.status = "APPROVED"
        po.approved_by = approved_by
        po.approved_at = timezone.now()

        po.save()

        return po

    @staticmethod
    @transaction.atomic
    def mark_ordered(po):

        if po.status != "APPROVED":
            raise ValueError(
                "Purchase Order must be approved first."
            )

        po.status = "ORDERED"
        po.save()

        return po

    @staticmethod
    @transaction.atomic
    def cancel(po):

        if po.status == "COMPLETED":
            raise ValueError(
                "Completed Purchase Orders cannot be cancelled."
            )

        po.status = "CANCELLED"
        po.save()

        return po
    @staticmethod
    @transaction.atomic
    def calculate_totals(po):
      subtotal = 0
      tax = 0
      discount = 0
      for item in po.items.all():
        subtotal += (
                item.unit_price * item.quantity
            )

        tax += item.tax_amount
        discount += item.discount_amount

      po.subtotal = subtotal
      po.tax_amount = tax
      po.discount_amount = discount

      po.total_amount = (
            subtotal
            + tax
            - discount
        )

      po.save()

      return po
    @staticmethod
    def validate_purchase_number(number):
      exists = PurchaseOrder.objects.filter(
            purchase_number=number
        ).exists()

      if exists:
          raise ValueError(
                "Purchase number already exists."
            ) 
    @staticmethod
    @transaction.atomic
    def create_purchase_order(**validated_data):
       PurchaseOrderService.validate_purchase_number(
            validated_data["purchase_number"]
        )

       return PurchaseOrder.objects.create(
            **validated_data
        )
    @staticmethod
    def validate_supplier(supplier):

        if supplier.status != "ACTIVE":
            raise ValueError(
                "Cannot create Purchase Order for inactive supplier."
            )
class GoodsReceiptService:
    """
    Process Goods Receipt.
    """

    @staticmethod
    @transaction.atomic
    def receive_items(
        goods_receipt,
        items,
    ):
        """
        items = [
            {
                "purchase_item": PurchaseOrderItem,
                "quantity": 5,
            }
        ]
        """

        for entry in items:

            purchase_item = entry["purchase_item"]
            received_qty = entry["quantity"]

            stock, created = Stock.objects.get_or_create(
                warehouse=goods_receipt.warehouse,
                product=purchase_item.product,
                defaults={
                    "quantity": 0,
                },
            )

            stock.quantity += received_qty
            stock.save()

            StockMovement.objects.create(
                warehouse=goods_receipt.warehouse,
                product=purchase_item.product,
                movement_type="IN",
                quantity=received_qty,
                remarks=f"GRN {goods_receipt.receipt_number}",
            )

            purchase_item.received_quantity += received_qty
            purchase_item.save()

        GoodsReceiptService.update_purchase_order_status(
            goods_receipt.purchase_order
        )
    @staticmethod
    def update_purchase_order_status(po):
      items = po.items.all()
      if not items.exists():
        return

      total = items.count()

      completed = sum(
            1
            for item in items
            if item.remaining_quantity == 0
        )

      if completed == total:
            po.status = "COMPLETED"

      elif completed > 0:
            po.status = "PARTIALLY_RECEIVED"

      po.save()