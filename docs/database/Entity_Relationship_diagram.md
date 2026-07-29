# Entity Relationship Diagram (ERD)

**Project Name:** AetherERP AI

**Document Version:** 1.0

**Document ID:** DB-003

**Prepared By:** Tejas M

**Phase:** Day 4 - Database Design & UML Modeling

---

# 1. Introduction

## Purpose

This document defines the complete Entity Relationship Diagram of AetherERP AI.

The ERD represents database entities and their relationships before implementation using PostgreSQL and Django ORM.

---

# 2. Database Relationship Overview
                     ORGANIZATION
                          |
      ------------------------------------------------
      |              |              |                |
      |              |              |                |
    Users          Branches     Departments      Products
      |                             |                |
      |                             |                |
    Roles                       Employees        Categories
      |                             |
      |                -------------------------
      |                |           |            |
 Permissions       Attendance    Leave      Payroll


                     PRODUCTS
                        |
                        |
                     Inventory
                        |
                        |
                   Warehouses


                     SUPPLIERS
                        |
                        |
                Purchase Orders
                        |
                        |
                Purchase Items
                        |
                        |
                     Products


                     CUSTOMERS
                        |
                        |
                  Sales Orders
                        |
                        |
                     Invoice
                        |
                        |
                     Payment


                     FINANCE
                        |
                        |
                  Transactions


                     AI SYSTEM
                        |
                        |
                  Dataset
                        |
                        |
                   AI Models
                        |
                        |
                  Predictions


                     USERS
                        |
                        |
                   Audit Logs
---

# 3. Entity Relationships

---

# Organization Relationships

## Organization → User

Relationship:


One Organization

    |

    |

Many Users


Type:


One-to-Many


Foreign Key:


User.organization_id


---

## Organization → Branch

Relationship:


Organization

 1

 |

 *

Branch


Foreign Key:


Branch.organization_id


---

## Organization → Department

Relationship:


Organization

 1

 |

 *

Department


Foreign Key:


Department.organization_id


---

## Organization → Product

Relationship:


Organization

 1

 |

 *

Product


Foreign Key:


Product.organization_id


---

# User Management Relationships

## Role → User


Role

1

|

User


Foreign Key:


User.role_id


---

## Role → Permission


Role

|

Permission


Relationship:


Many-to-Many


Intermediate Table:


role_permissions


---

## User → Audit Log


User

1

|

AuditLog


Foreign Key:


AuditLog.user_id


---

# HR Relationships

## Department → Employee


Department

 1

 |

 *

Employee


Foreign Key:


Employee.department_id


---

## Employee → Attendance


Employee

1

|

*

Attendance


Foreign Key:


Attendance.employee_id


---

## Employee → Leave Request


Employee

1

|

*

LeaveRequest


Foreign Key:


LeaveRequest.employee_id


---

## Employee → Payroll


Employee

1

|

*

Payroll


Foreign Key:


Payroll.employee_id


---

# Inventory Relationships

## Category → Product


Category

1

|

Product


Foreign Key:


Product.category_id


---

## Product → Stock


Product

1

|

*

Stock


Foreign Key:


Stock.product_id


---

## Warehouse → Stock


Warehouse

 1

 |

 *

Stock


Foreign Key:


Stock.warehouse_id


---

# Supplier & Purchase Relationships

## Supplier → Purchase Order


Supplier

1

|

*

Purchase Order


Foreign Key:


PurchaseOrder.supplier_id


---

## Purchase Order → Purchase Item


Purchase Order

   1

   |

   *

Purchase Item


Foreign Key:


PurchaseItem.purchase_order_id


---

## Product → Purchase Item


Product

1

|

*

Purchase Item


Foreign Key:


PurchaseItem.product_id


---

# Customer & Sales Relationships

## Customer → Sales Order


Customer

1

|

*

Sales Order


Foreign Key:


SalesOrder.customer_id


---

## Sales Order → Invoice


Sales Order

  1

  |

  1

Invoice


Relationship:


One-to-One


Foreign Key:


Invoice.sales_order_id


---

## Invoice → Payment


Invoice

1

|

Payment


Foreign Key:


Payment.invoice_id


---

# Finance Relationships

## Transaction Relationships

Finance receives data from:


Sales

Purchase

Payroll

Expense


Structure:


Transaction

id

organization_id

reference_type

reference_id

amount

date


---

# AI Relationships

## Organization → Dataset


Organization

  1

  |

  *

Dataset


---

## Dataset → AI Model


Dataset

1

|

*

AI Model


---

## AI Model → Prediction


AI Model

 1

 |

 *

Prediction


---

# 4. Complete Database Relationship Map


Organization
│
├── Users
│ │
│ ├── Roles
│ │ │
│ │ └── Permissions
│ │
│ └── Audit Logs
│
├── Branches
│
├── Departments
│ │
│ └── Employees
│ │
│ ├── Attendance
│ |
│ ├── Leave Requests
│ |
│ └── Payroll
│
├── Products
│ │
│ ├── Categories
│ |
│ └── Inventory
│ |
│ └── Warehouses
│
├── Suppliers
│ |
│ └── Purchase Orders
│ |
│ └── Purchase Items
│
├── Customers
│ |
│ └── Sales Orders
│ |
│ └── Invoices
│ |
│ └── Payments
│
├── Finance
│ |
│ └── Transactions
│
└── AI System
|
├── Dataset
|
├── AI Models
|
└── Predictions


---

# 5. ERD Design Rules

The database follows:

- Every business table connects to Organization
- Foreign keys maintain data integrity
- No duplicate business data
- Audit tracking for important actions
- Soft deletion instead of permanent deletion
- UUID support for external references

---

# 6. Future ERD Expansion

Future modules can connect with existing entities:


Manufacturing
|
Products

Asset Management
|
Employees

CRM
|
Customers

Mobile App
|
Users


---

# 7. Conclusion

The ERD provides the complete database relationship structure of AetherERP AI. It acts as the foundation for PostgreSQL schema creation and Django model development.

All future database implementation will follow this relationship design.