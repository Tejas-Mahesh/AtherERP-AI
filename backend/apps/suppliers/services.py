from django.db import transaction

from .models import Supplier


class SupplierService:

    @staticmethod
    def validate_supplier_code(code):

        if Supplier.objects.filter(
            supplier_code=code
        ).exists():

            raise ValueError(
                "Supplier code already exists."
            )

    @staticmethod
    def validate_email(email):

        if email:

            if Supplier.objects.filter(
                email=email
            ).exists():

                raise ValueError(
                    "Supplier email already exists."
                )

    @staticmethod
    @transaction.atomic
    def create_supplier(**validated_data):

        validated_data["supplier_code"] = (
            SupplierService.generate_supplier_code()
        )

        SupplierService.validate_email(
            validated_data.get("email")
        )

        return Supplier.objects.create(
            **validated_data
        )
    @staticmethod
    def generate_supplier_code():
      last_supplier = Supplier.objects.order_by(
            "-supplier_code"
        ).first()

      if not last_supplier:
            return "SUP-000001"

      last_number = int(
            last_supplier.supplier_code.split("-")[1]
        )

      return f"SUP-{last_number + 1:06d}"