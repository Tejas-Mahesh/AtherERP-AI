from rest_framework.permissions import BasePermission


class IsSuperAdmin(BasePermission):
    """
    Allows access only to Django Superusers.
    """

    message = "Only Super Administrators can perform this action."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_superuser
        )


class IsOrganizationUser(BasePermission):
    """
    User must belong to an organization.
    """

    message = "You are not assigned to any organization."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.organization is not None
        )


class HasRole(BasePermission):
    """
    User must have a role assigned.
    """

    message = "No role assigned."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role is not None
        )


class HasModelPermission(BasePermission):
    """
    Uses Django model permissions.

    Set:

        required_permission = "app_label.permission_codename"

    inside the ViewSet.
    """

    message = "Permission denied."

    def has_permission(self, request, view):

        permission = getattr(
            view,
            "required_permission",
            None,
        )

        if permission is None:
            return True

        return (
            request.user.is_authenticated
            and request.user.has_perm(permission)
        )


class IsAdminOrReadOnly(BasePermission):
    """
    Everyone can read.
    Only Staff/Admin can modify.
    """

    def has_permission(self, request, view):

        if request.method in (
            "GET",
            "HEAD",
            "OPTIONS",
        ):
            return True

        return (
            request.user.is_authenticated
            and request.user.is_staff
        )


class IsOwnerOrReadOnly(BasePermission):
    """
    Users may edit only their own record.
    """

    def has_object_permission(
        self,
        request,
        view,
        obj,
    ):

        if request.method in (
            "GET",
            "HEAD",
            "OPTIONS",
        ):
            return True

        return obj == request.user