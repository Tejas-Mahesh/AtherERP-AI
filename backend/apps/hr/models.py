from django.db import models

from apps.common.models import BaseModel
from apps.organizations.models import Organization
from apps.accounts.models import User


class Department(BaseModel):
    """
    Department within an organization.
    """

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="departments"
    )

    name = models.CharField(
        max_length=150
    )

    code = models.CharField(
        max_length=20
    )

    description = models.TextField(
        blank=True
    )

    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_departments"
    )

    class Meta:
       ordering = ["name"]

       constraints = [
        models.UniqueConstraint(
            fields=["organization", "code"],
            name="unique_department_code_per_organization",
        )
    ]

    def __str__(self):
        return f"{self.name} ({self.organization.name})"

class Designation(BaseModel):
    """
    Job designation within a department.
    """

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="designations"
    )

    name = models.CharField(
        max_length=150
    )

    code = models.CharField(
        max_length=20
    )

    level = models.PositiveIntegerField(
        default=1,
        help_text="Hierarchy level. Lower numbers indicate junior positions."
    )

    description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ["level", "name"]

        constraints = [
            models.UniqueConstraint(
                fields=["department", "code"],
                name="unique_designation_code_per_department",
            )
        ]

    def __str__(self):
        return f"{self.name} - {self.department.name}"

class Employee(BaseModel):
    """
    Employee profile.
    """

    EMPLOYMENT_TYPES = [
        ("FULL_TIME", "Full Time"),
        ("PART_TIME", "Part Time"),
        ("CONTRACT", "Contract"),
        ("INTERN", "Intern"),
    ]

    EMPLOYMENT_STATUS = [
        ("ACTIVE", "Active"),
        ("ON_LEAVE", "On Leave"),
        ("RESIGNED", "Resigned"),
        ("TERMINATED", "Terminated"),
    ]

    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    ]

    employee_id = models.CharField(
        max_length=20,
        unique=True,
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employee_profile",
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="employees",
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    designation = models.ForeignKey(
        Designation,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    manager = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="team_members",
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )

    date_of_birth = models.DateField()

    joining_date = models.DateField()

    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPES,
        default="FULL_TIME",
    )

    employment_status = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_STATUS,
        default="ACTIVE",
    )

    phone = models.CharField(
        max_length=15,
    )

    alternate_phone = models.CharField(
        max_length=15,
        blank=True,
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100,
    )

    state = models.CharField(
        max_length=100,
    )

    country = models.CharField(
        max_length=100,
        default="India",
    )

    postal_code = models.CharField(
        max_length=10,
    )

    profile_photo = models.ImageField(
        upload_to="employees/",
        blank=True,
        null=True,
    )

    basic_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    bank_name = models.CharField(
        max_length=150,
        blank=True,
    )

    account_number = models.CharField(
        max_length=50,
        blank=True,
    )

    ifsc_code = models.CharField(
        max_length=20,
        blank=True,
    )

    pan_number = models.CharField(
        max_length=20,
        blank=True,
    )

    aadhaar_number = models.CharField(
        max_length=20,
        blank=True,
    )

    emergency_contact_name = models.CharField(
        max_length=150,
        blank=True,
    )

    emergency_contact_relationship = models.CharField(
        max_length=100,
        blank=True,
    )

    emergency_contact_phone = models.CharField(
        max_length=15,
        blank=True,
    )

    def __str__(self):
        return f"{self.employee_id} - {self.user.get_full_name()}"