# Database Entity Planning Document

**Project Name:** AetherERP AI

**Document Version:** 1.0

**Document ID:** DB-002

**Prepared By:** Tejas M

**Phase:** Day 4 - Database Design & UML Modeling

---

# 1. Introduction

## Purpose

This document defines the planned database structure and relationships between entities.

It acts as a blueprint before creating PostgreSQL tables and Django models.

---

# 2. Database Design Strategy

The database follows:

- Relational Database Model
- PostgreSQL
- Django ORM
- Normalization
- Foreign Key Relationships
- Multi-Tenant Data Isolation

---

# 3. Organization Structure
|
|
+---- Branch

|
|
+---- User

|
|
+---- Department

---

# 4. User Structure

|
|
+---- User

          |
          |
      Audit Log


---

# 5. Employee Structure
Department
  |
  |
Employee
  |
  |
Attendence
  |
  |
Leave
  |
  |
Payroll


---

# 6. Inventory Structure
Category 
 |
 |
Product
 |
 |
Stock
 |
 |
Warehouse

---

# 7. Purchase Structure

Supplier
|
|
Purchase Order
|
|
Purchase item 
|
|
Product

---

# 8. Sales Structure

Customer
 |
 |
Sales order
 |
 |
Invoice
 |
 |
Payment

---

# 9. Finance Structure
Sales

|

Transaction

Purchase

|

Transaction

Payroll

|

Transaction


---

# 10. AI Data Structure
ERP Business Data

    |

    |

AI Dataset

    |

    |

AI Model

    |

    |

Prediction Result

---

# 11. Common Fields

All major tables inherit:

id

uuid

created_at

updated_at

created_by

updated_by

is_active

---

# 12. Multi-Tenant Design

All business-related tables contain:
organization_id


Example:


Employee

id

organization_id

name


This ensures organizations cannot access each other's data.

---

# 13. Relationship Types

## One-to-One

Examples:


User

|

Employee


---

## One-to-Many

Examples:


Organization

|

Many Employees


---

## Many-to-Many

Examples:


Role

|

Permission


---

# 14. Future Expansion Support

The design allows adding:

- Manufacturing
- Asset Management
- Project Management
- Customer Portal
- Mobile Application
- Advanced AI Services

without changing existing database architecture.

---

# 15. Conclusion
Database Entity Planning defines the relationship structure of AetherERP AI. This blueprint will guide the creation of PostgreSQL tables, Django models, migrations, and API development.
 