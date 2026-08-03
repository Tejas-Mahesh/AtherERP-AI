from django.db import transaction

from apps.inventory.models import StockTransaction


class StockTransactionService:
    """
    Service responsible for recording every inventory movement.

    This acts as the Inventory Ledger.

    Every module should create stock transactions only
    through this service.
    """

    @staticmethod
    @transaction.atomic
    def create_transaction(
        *,
        product,
        warehouse,
        transaction_type,
        quantity,
        location=None,
        reference_number="",
        remarks="",
        created_by=None,
    ):
        """
        Generic transaction creator.

        Used by:
            - Purchases
            - Sales
            - Purchase Returns
            - Sales Returns
            - Stock Adjustments
            - Stock Transfers
            - Opening Stock
        """

        return StockTransaction.objects.create(
            product=product,
            warehouse=warehouse,
            location=location,
            transaction_type=transaction_type,
            quantity=quantity,
            reference_number=reference_number,
            remarks=remarks,
            created_by=created_by,
        )

    # -----------------------------
    # Purchase
    # -----------------------------

    @staticmethod
    def purchase(
        *,
        product,
        warehouse,
        quantity,
        reference_number,
        location=None,
        created_by=None,
    ):
        return StockTransactionService.create_transaction(
            product=product,
            warehouse=warehouse,
            location=location,
            transaction_type="PURCHASE",
            quantity=quantity,
            reference_number=reference_number,
            remarks="Purchase Receipt",
            created_by=created_by,
        )

    # -----------------------------
    # Sale
    # -----------------------------

    @staticmethod
    def sale(
        *,
        product,
        warehouse,
        quantity,
        reference_number,
        location=None,
        created_by=None,
    ):
        return StockTransactionService.create_transaction(
            product=product,
            warehouse=warehouse,
            location=location,
            transaction_type="SALE",
            quantity=quantity,
            reference_number=reference_number,
            remarks="Sales Invoice",
            created_by=created_by,
        )

    # -----------------------------
    # Adjustment
    # -----------------------------

    @staticmethod
    def adjustment(
        *,
        product,
        warehouse,
        quantity,
        reference_number,
        remarks,
        location=None,
        created_by=None,
    ):
        return StockTransactionService.create_transaction(
            product=product,
            warehouse=warehouse,
            location=location,
            transaction_type="ADJUSTMENT",
            quantity=quantity,
            reference_number=reference_number,
            remarks=remarks,
            created_by=created_by,
        )

    # -----------------------------
    # Opening Stock
    # -----------------------------

    @staticmethod
    def opening_stock(
        *,
        product,
        warehouse,
        quantity,
        location=None,
        created_by=None,
    ):
        return StockTransactionService.create_transaction(
            product=product,
            warehouse=warehouse,
            location=location,
            transaction_type="OPENING",
            quantity=quantity,
            reference_number="OPENING",
            remarks="Opening Stock",
            created_by=created_by,
        )

    # -----------------------------
    # Transfer In
    # -----------------------------

    @staticmethod
    def transfer_in(
        *,
        product,
        warehouse,
        quantity,
        reference_number,
        location=None,
        created_by=None,
    ):
        return StockTransactionService.create_transaction(
            product=product,
            warehouse=warehouse,
            location=location,
            transaction_type="TRANSFER_IN",
            quantity=quantity,
            reference_number=reference_number,
            remarks="Warehouse Transfer In",
            created_by=created_by,
        )

    # -----------------------------
    # Transfer Out
    # -----------------------------

    @staticmethod
    def transfer_out(
        *,
        product,
        warehouse,
        quantity,
        reference_number,
        location=None,
        created_by=None,
    ):
        return StockTransactionService.create_transaction(
            product=product,
            warehouse=warehouse,
            location=location,
            transaction_type="TRANSFER_OUT",
            quantity=quantity,
            reference_number=reference_number,
            remarks="Warehouse Transfer Out",
            created_by=created_by,
        )

    # -----------------------------
    # Purchase Return
    # -----------------------------

    @staticmethod
    def purchase_return(
        *,
        product,
        warehouse,
        quantity,
        reference_number,
        location=None,
        created_by=None,
    ):
        return StockTransactionService.create_transaction(
            product=product,
            warehouse=warehouse,
            location=location,
            transaction_type="RETURN_OUT",
            quantity=quantity,
            reference_number=reference_number,
            remarks="Purchase Return",
            created_by=created_by,
        )

    # -----------------------------
    # Sales Return
    # -----------------------------

    @staticmethod
    def sales_return(
        *,
        product,
        warehouse,
        quantity,
        reference_number,
        location=None,
        created_by=None,
    ):
        return StockTransactionService.create_transaction(
            product=product,
            warehouse=warehouse,
            location=location,
            transaction_type="RETURN_IN",
            quantity=quantity,
            reference_number=reference_number,
            remarks="Sales Return",
            created_by=created_by,
        )