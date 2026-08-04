from rest_framework.permissions import BasePermission


class IsSuperAdmin(BasePermission):
    """
    Allows access only to Superusers.
    """

    message = (
        "Only Super Administrators can perform this action."
    )

    def has_permission(
        self,
        request,
        view,
    ):
        return (
            request.user.is_authenticated
            and request.user.is_superuser
        )


class IsOrganizationAdmin(BasePermission):
    """
    Allows access only to Organization Admins.
    """

    message = (
        "Only Organization Administrators can perform this action."
    )

    def has_permission(
        self,
        request,
        view,
    ):
        return (
            request.user.is_authenticated
            and getattr(
                request.user,
                "user_type",
                None,
            )
            == "ADMIN"
        )


class IsOrganizationMember(BasePermission):
    """
    Any authenticated organization user.
    """

    message = (
        "You must belong to an organization."
    )

    def has_permission(
        self,
        request,
        view,
    ):
        return request.user.is_authenticated


class ReadOnly(BasePermission):
    """
    Allow read-only requests.
    """

    def has_permission(
        self,
        request,
        view,
    ):
        return request.method in (
            "GET",
            "HEAD",
            "OPTIONS",
        )


class IsAdminOrReadOnly(BasePermission):
    """
    Anyone can read.
    Only Organization Admin can modify.
    """

    def has_permission(
        self,
        request,
        view,
    ):

        if request.method in (
            "GET",
            "HEAD",
            "OPTIONS",
        ):
            return True

        return (
            request.user.is_authenticated
            and getattr(
                request.user,
                "user_type",
                None,
            )
            == "ADMIN"
        )