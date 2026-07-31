from django.db import transaction

from .models import Employee


class EmployeeService:
    """
    Business logic for Employee operations.
    """

    @staticmethod
    @transaction.atomic
    def create_employee(**validated_data):
        """
        Create a new employee.
        """

        employee = Employee.objects.create(**validated_data)

        return employee

    @staticmethod
    @transaction.atomic
    def update_employee(employee, **validated_data):
        """
        Update employee information.
        """

        for field, value in validated_data.items():
            setattr(employee, field, value)

        employee.save()

        return employee

    @staticmethod
    @transaction.atomic
    def deactivate_employee(employee):
        """
        Deactivate employee.
        """

        employee.is_active = False
        employee.save()

        return employee

    @staticmethod
    @transaction.atomic
    def activate_employee(employee):
        """
        Activate employee.
        """

        employee.is_active = True
        employee.save()

        return employee