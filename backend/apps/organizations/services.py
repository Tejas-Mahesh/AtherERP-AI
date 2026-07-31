from django.db import transaction

from .models import Organization, Branch, Location


class OrganizationService:
    """
    Business logic for Organization operations.
    """

    @staticmethod
    @transaction.atomic
    def create_organization(**validated_data):
        return Organization.objects.create(**validated_data)

    @staticmethod
    @transaction.atomic
    def update_organization(instance, **validated_data):

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()

        return instance

    @staticmethod
    @transaction.atomic
    def deactivate_organization(instance):
        instance.is_active = False
        instance.save()
        return instance

    @staticmethod
    @transaction.atomic
    def activate_organization(instance):
        instance.is_active = True
        instance.save()
        return instance


class BranchService:

    @staticmethod
    @transaction.atomic
    def create_branch(**validated_data):
        return Branch.objects.create(**validated_data)

    @staticmethod
    @transaction.atomic
    def update_branch(instance, **validated_data):

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()

        return instance


class LocationService:

    @staticmethod
    @transaction.atomic
    def create_location(**validated_data):
        return Location.objects.create(**validated_data)

    @staticmethod
    @transaction.atomic
    def update_location(instance, **validated_data):

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()

        return instance