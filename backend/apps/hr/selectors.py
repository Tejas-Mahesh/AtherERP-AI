from .models import Employee


class EmployeeSelector:
    """
    Read operations for Employee.
    """

    @staticmethod
    def get_employee(employee_id):
        return Employee.objects.select_related(
            "user",
            "organization",
            "department",
            "designation",
        ).get(id=employee_id)

    @staticmethod
    def get_all_employees():
        return Employee.objects.select_related(
            "user",
            "organization",
            "department",
            "designation",
        )

    @staticmethod
    def get_active_employees():
        return Employee.objects.filter(
            is_active=True
        ).select_related(
            "user",
            "organization",
            "department",
            "designation",
        )