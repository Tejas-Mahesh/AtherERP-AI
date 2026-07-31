from .models import Organization, Branch, Location


class OrganizationSelector:

    @staticmethod
    def get_all():
        return Organization.objects.all()

    @staticmethod
    def get_by_id(pk):
        return Organization.objects.get(pk=pk)


class BranchSelector:

    @staticmethod
    def get_all():
        return Branch.objects.select_related(
            "organization"
        )

    @staticmethod
    def get_by_id(pk):
        return Branch.objects.select_related(
            "organization"
        ).get(pk=pk)


class LocationSelector:

    @staticmethod
    def get_all():
        return Location.objects.select_related(
            "branch",
            "branch__organization",
        )

    @staticmethod
    def get_by_id(pk):
        return Location.objects.select_related(
            "branch",
            "branch__organization",
        ).get(pk=pk)