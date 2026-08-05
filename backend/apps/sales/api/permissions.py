from rest_framework.permissions import BasePermission


class SalesPermission(BasePermission):
    """
    Permission class for Sales module.
    """

    message = (
        "You do not have permission "
        "to access the Sales module."
    )

    def has_permission(
        self,
        request,
        view,
    ):
        """
        Module-level permission.
        """

        user = request.user

        if not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        if user.is_staff:
            return True

        return True

    def has_object_permission(
        self,
        request,
        view,
        obj,
    ):
        """
        Object-level permission.
        """

        user = request.user

        if user.is_superuser:
            return True

        return True