from django.db import transaction


class QuotationStatusService:
    """
    Handles Quotation status transitions.
    """

    @staticmethod
    @transaction.atomic
    def update_status(quotation):
        """
        Update quotation status automatically.
        """

        if quotation.status == "CONVERTED":
            return quotation

        if quotation.valid_until < quotation.quotation_date:
            quotation.status = "EXPIRED"
            quotation.save()

        return quotation

    @staticmethod
    @transaction.atomic
    def mark_submitted(quotation):

        if quotation.status != "DRAFT":
            raise ValueError(
                "Only draft quotations can be submitted."
            )

        quotation.status = "SUBMITTED"
        quotation.save()

        return quotation

    @staticmethod
    @transaction.atomic
    def mark_approved(quotation):

        if quotation.status != "SUBMITTED":
            raise ValueError(
                "Only submitted quotations can be approved."
            )

        quotation.status = "APPROVED"
        quotation.save()

        return quotation

    @staticmethod
    @transaction.atomic
    def mark_rejected(quotation):

        if quotation.status not in [
            "DRAFT",
            "SUBMITTED",
        ]:
            raise ValueError(
                "Quotation cannot be rejected."
            )

        quotation.status = "REJECTED"
        quotation.save()

        return quotation

    @staticmethod
    @transaction.atomic
    def mark_expired(quotation):

        if quotation.status in [
            "CONVERTED",
            "REJECTED",
        ]:
            raise ValueError(
                "Quotation cannot be expired."
            )

        quotation.status = "EXPIRED"
        quotation.save()

        return quotation

    @staticmethod
    @transaction.atomic
    def mark_converted(quotation):

        if quotation.status != "APPROVED":
            raise ValueError(
                "Only approved quotations can be converted."
            )

        quotation.status = "CONVERTED"
        quotation.save()

        return quotation