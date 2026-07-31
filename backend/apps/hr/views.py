from rest_framework import viewsets

from .models import Employee
from .serializers import EmployeeSerializer
from .services import EmployeeService

from .selectors import EmployeeSelector
class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = EmployeeSelector.get_all_employees()

    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        EmployeeService.create_employee(
            **serializer.validated_data
        )

    def perform_update(self, serializer):
        EmployeeService.update_employee(
            self.get_object(),
            **serializer.validated_data
        )