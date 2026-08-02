from .models import (
    Supplier,
    SupplierContact,
    SupplierBankAccount,
    SupplierDocument,
)


class SupplierSelector:

    @staticmethod
    def get_all():

        return Supplier.objects.select_related(
            "organization",
        )

    @staticmethod
    def get_by_id(pk):

        return Supplier.objects.select_related(
            "organization",
        ).prefetch_related(
            "contacts",
            "bank_accounts",
            "documents",
        ).get(pk=pk)

    @staticmethod
    def get_active():

        return Supplier.objects.filter(
            status="ACTIVE",
        )


class SupplierContactSelector:

    @staticmethod
    def get_by_supplier(supplier):

        return SupplierContact.objects.filter(
            supplier=supplier,
        )


class SupplierBankAccountSelector:

    @staticmethod
    def get_default_account(supplier):

        return SupplierBankAccount.objects.filter(
            supplier=supplier,
            is_default=True,
        ).first()


class SupplierDocumentSelector:

    @staticmethod
    def get_documents(supplier):

        return SupplierDocument.objects.filter(
            supplier=supplier,
        )