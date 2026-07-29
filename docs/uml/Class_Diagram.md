# UML Class Diagram

**Project Name:** AetherERP AI

**Document Version:** 1.0

**Document ID:** UML-001

**Prepared By:** Tejas M

**Phase:** Day 4 - Database Design & UML Modeling

---

# 1. Introduction

## Purpose

This document defines the UML Class Diagram of AetherERP AI.

The purpose is to represent the planned Django model structure before implementation.

The class diagram describes:

- Model classes
- Attributes
- Relationships
- Methods
- Inheritance structure

---

# 2. Base Model Architecture

All major models inherit common fields.
             BaseModel

                 |
 --------------------------------
 |              |               |

Organization Employee Product
User Invoice Customer

---

# 3. BaseModel Class


Class BaseModel

Attributes:

id
uuid
created_at
updated_at
created_by
updated_by
is_active

Methods:

save()
delete()

Purpose:

Provides common fields and behavior for all database models.

---

# 4. Organization Module Classes

## Organization


Class Organization

Attributes:

name
email
phone
address
website
subscription_plan

Methods:

create_branch()
manage_users()

Relationships:


Organization

1

|

Branch


---

## Branch


Class Branch

Attributes:

name
location
phone

Methods:

update_details()

---

# 5. User Management Classes

## User


Class User

Attributes:

username
email
password
role
is_active
last_login

Methods:

authenticate()
change_password()
logout()

Relationships:


Organization

1

|

User


---

## Role


Class Role

Attributes:

name
description

Methods:

assign_permission()

Relationship:


Role

|

Permission


---

## Permission


Class Permission

Attributes:

name
code

---

# 6. HR Module Classes

## Department


Class Department

Attributes:

name
description

Methods:

add_employee()

---

## Designation


Class Designation

Attributes:

title

---

## Employee


Class Employee

Attributes:

employee_code
first_name
last_name
email
phone
joining_date
salary
status

Methods:

update_profile()
calculate_salary()

Relationships:


Department

1

|

Employee


---

# 7. Attendance Classes

## Attendance


Class Attendance

Attributes:

date
check_in
check_out
status

Methods:

mark_attendance()
generate_report()

Relationship:


Employee

1

|

Attendance


---

# 8. Leave Management Classes

## LeaveRequest


Class LeaveRequest

Attributes:

start_date
end_date
reason
status

Methods:

submit_request()
approve_leave()
reject_leave()

Relationship:


Employee

1

|

LeaveRequest


---

# 9. Payroll Classes

## Payroll


Class Payroll

Attributes:

month
basic_salary
allowance
deduction
net_salary
status

Methods:

calculate_salary()
generate_payslip()

Relationship:


Employee

1

|

Payroll


---

# 10. Inventory Classes

## Category


Class Category

Attributes:

name

Methods:

add_product()

---

## Product


Class Product

Attributes:

name
sku
price
quantity

Methods:

update_stock()
check_availability()

Relationship:


Category

1

|

Product


---

## Warehouse


Class Warehouse

Attributes:

name
location

Methods:

transfer_stock()

---

## Stock


Class Stock

Attributes:

quantity

Methods:

increase_stock()
decrease_stock()

Relationships:


Product

1

|

Stock

Warehouse

1

|

Stock


---

# 11. Purchase Classes

## Supplier


Class Supplier

Attributes:

name
email
phone
address

Methods:

create_purchase_order()

---

## PurchaseOrder


Class PurchaseOrder

Attributes:

order_date
status
total_amount

Methods:

approve_order()
receive_goods()

---

## PurchaseItem


Class PurchaseItem

Attributes:

quantity
price

Relationship:


PurchaseOrder

1

|

PurchaseItem


---

# 12. Sales Classes

## Customer


Class Customer

Attributes:

name
email
phone
address

Methods:

create_order()

---

## SalesOrder


Class SalesOrder

Attributes:

order_date
status
total_amount

Methods:

confirm_order()
cancel_order()

---

## Invoice


Class Invoice

Attributes:

invoice_number
amount
status

Methods:

generate_invoice()
calculate_total()

---

## Payment


Class Payment

Attributes:

amount
payment_date
payment_method

Methods:

process_payment()

---

# 13. Finance Classes

## Transaction


Class Transaction

Attributes:

transaction_type
amount
date
reference

Methods:

record_transaction()

---

# 14. AI Classes

## AIModel


Class AIModel

Attributes:

name
version
algorithm
accuracy

Methods:

train()
evaluate()
predict()

---

## Dataset


Class Dataset

Attributes:

name
source
created_date

Methods:

preprocess()

---

## Prediction


Class Prediction

Attributes:

prediction_type
input_data
result

Methods:

generate_prediction()

---

# 15. System Classes

## Notification


Class Notification

Attributes:

title
message
status

Methods:

send()
mark_read()

---

## AuditLog


Class AuditLog

Attributes:

action
module
timestamp
ip_address

Methods:

record_activity()

---

# 16. Complete Class Relationship Diagram

                Organization
                     |
                     |
   ------------------------------------
   |              |                   |
  User          Branch            Department
   |                                  |
  Role                              Employee
   |                                  |

Permission -------------------
| | |
Attendance Leave Payroll

Organization

   |

Product

   |

Category

   |

 Stock

   |

Warehouse

Supplier

   |

PurchaseOrder

   |

PurchaseItem

   |

Product

Customer

   |

SalesOrder

   |

Invoice

   |

Payment

Organization

   |

Dataset

   |

AIModel

   |

Prediction


---

# 17. Design Patterns Used

## Model Inheritance


BaseModel

  ↓

All Business Models


---

## Service Pattern

Business logic will not be written inside models.

Example:


EmployeeService

PayrollService

InventoryService

SalesService


---

## Repository Pattern

Database operations are separated.

Example:


EmployeeRepository

ProductRepository


---

# 18. Conclusion

The UML Class Diagram defines the object-oriented structure of AetherERP AI.

This design will guide:

- Django model creation
- Application structure
- Service layer development
- API implementation
- Testing strategy

The next implementation phase will convert these classes into actual Django models.