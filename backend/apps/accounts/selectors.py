from .models import User, UserProfile, Role


class UserSelector:

    @staticmethod
    def get_all():

        return User.objects.select_related(
            "organization",
            "role",
        )

    @staticmethod
    def get_by_id(pk):

        return User.objects.select_related(
            "organization",
            "role",
        ).get(pk=pk)

    @staticmethod
    def get_by_email(email):

        return User.objects.select_related(
            "organization",
            "role",
        ).get(email=email)


class UserProfileSelector:

    @staticmethod
    def get_all():

        return UserProfile.objects.select_related(
            "user",
        )

    @staticmethod
    def get_by_id(pk):

        return UserProfile.objects.select_related(
            "user",
        ).get(pk=pk)


class RoleSelector:

    @staticmethod
    def get_all():

        return Role.objects.prefetch_related(
            "permissions",
        ).select_related(
            "organization",
        )

    @staticmethod
    def get_by_id(pk):

        return Role.objects.prefetch_related(
            "permissions",
        ).select_related(
            "organization",
        ).get(pk=pk)