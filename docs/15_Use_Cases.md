# Use Cases

**Project Name:** AetherERP AI

**Document Version:** 1.0

**Document ID:** UCD-001

**Prepared By:** Tejas M

---

# 1. Introduction

This document describes the major use cases of AetherERP AI.

A use case explains how a user interacts with the system to accomplish a business goal.

Each use case contains:

- Use Case ID
- Use Case Name
- Primary Actor
- Description
- Preconditions
- Trigger
- Main Flow
- Alternative Flow
- Postconditions

---

# UC-001 User Login

## Primary Actor

User

## Description

Allows registered users to securely access the system.

## Preconditions

- User account exists.
- User account is active.

## Trigger

User clicks **Login**.

## Main Flow

1. User enters email.
2. User enters password.
3. System validates credentials.
4. System creates user session.
5. Dashboard is displayed.

## Alternative Flow

- Invalid email or password.
- Account is inactive.
- Account is locked.

## Postconditions

- User is authenticated.
- User dashboard is loaded.

---

# UC-002 User Logout

## Primary Actor

User

## Description

Ends the current user session.

## Preconditions

- User is logged in.

## Main Flow

1. User clicks Logout.
2. Session is destroyed.
3. Login page is displayed.

## Postconditions

- User is securely logged out.

---

# UC-003 Create Organization

## Primary Actor

Super Administrator

## Description

Creates a new organization.

## Preconditions

- Super Administrator is logged in.

## Main Flow

1. Open Organization Module.
2. Click Create Organization.
3. Enter organization details.
4. Save organization.
5. System creates organization.

## Alternative Flow

- Duplicate organization name.

## Postconditions

- Organization is available in the system.

---

# UC-004 Create Department

## Primary Actor

Organization Administrator

## Description

Creates departments inside an organization.

## Preconditions

- Organization exists.

## Main Flow

1. Open Departments.
2. Click Add Department.
3. Enter department information.
4. Save.

## Postconditions

- Department is created.

---

# UC-005 Add Employee

## Primary Actor

HR Manager

## Description

Registers a new employee.

## Preconditions

- Department exists.

## Main Flow

1. Open Employee Module.
2. Click Add Employee.
3. Enter employee details.
4. Upload documents.
5. Save employee.

## Alternative Flow

- Duplicate employee ID.
- Missing required fields.

## Postconditions

- Employee profile is created.

---

# UC-006 Record Attendance

## Primary Actor

HR Manager

## Description

Records daily employee attendance.

## Preconditions

- Employee exists.

## Main Flow

1. Open Attendance.
2. Select date.
3. Mark attendance.
4. Save.

## Alternative Flow

- Attendance already exists.

## Postconditions

- Attendance record stored.

---

# UC-007 Apply Leave

## Primary Actor

Employee

## Description

Allows employees to submit leave requests.

## Preconditions

- Employee is active.

## Main Flow

1. Open Leave Module.
2. Click Apply Leave.
3. Select leave dates.
4. Enter reason.
5. Submit request.

## Alternative Flow

- Insufficient leave balance.

## Postconditions

- Leave request created.

---

# UC-008 Approve Leave

## Primary Actor

HR Manager

## Description

Approves or rejects employee leave requests.

## Preconditions

- Leave request exists.

## Main Flow

1. Open Leave Requests.
2. Review application.
3. Approve or Reject.
4. Employee is notified.

## Postconditions

- Leave status updated.

---

# UC-009 Generate Payroll

## Primary Actor

HR Manager

## Description

Generates employee salaries.

## Preconditions

- Attendance finalized.

## Main Flow

1. Select payroll period.
2. Calculate salary.
3. Review deductions.
4. Generate payslips.
5. Save payroll.

## Postconditions

- Payroll generated.

---

# UC-010 Add Product

## Primary Actor

Inventory Manager

## Description

Adds new products.

## Preconditions

- Category exists.

## Main Flow

1. Open Product Module.
2. Click Add Product.
3. Enter details.
4. Save.

## Alternative Flow

- Duplicate product code.

## Postconditions

- Product added.

---

# UC-011 Receive Inventory

## Primary Actor

Inventory Manager

## Description

Records purchased inventory.

## Preconditions

- Purchase Order exists.

## Main Flow

1. Open Purchase Module.
2. Select Purchase Order.
3. Receive items.
4. Update stock.
5. Save.

## Postconditions

- Inventory increased.

---

# UC-012 Transfer Stock

## Primary Actor

Inventory Manager

## Description

Transfers products between warehouses.

## Preconditions

- Stock available.

## Main Flow

1. Select source warehouse.
2. Select destination warehouse.
3. Choose products.
4. Enter quantity.
5. Confirm transfer.

## Alternative Flow

- Insufficient stock.

## Postconditions

- Warehouse stock updated.

---

# UC-013 Register Customer

## Primary Actor

Sales Manager

## Description

Registers customers.

## Preconditions

- User authenticated.

## Main Flow

1. Open Customer Module.
2. Add customer.
3. Save.

## Postconditions

- Customer profile created.

---

# UC-014 Create Sales Order

## Primary Actor

Sales Manager

## Description

Creates customer sales orders.

## Preconditions

- Customer exists.
- Products available.

## Main Flow

1. Select customer.
2. Add products.
3. Calculate total.
4. Save order.

## Alternative Flow

- Product unavailable.

## Postconditions

- Sales order created.

---

# UC-015 Generate Invoice

## Primary Actor

Sales Manager

## Description

Creates invoices for confirmed orders.

## Preconditions

- Sales order approved.

## Main Flow

1. Select order.
2. Generate invoice.
3. Save invoice.

## Postconditions

- Invoice available.

---

# UC-016 Record Payment

## Primary Actor

Finance Manager

## Description

Records customer payments.

## Preconditions

- Invoice exists.

## Main Flow

1. Open Invoice.
2. Enter payment.
3. Select payment method.
4. Save.

## Postconditions

- Invoice status updated.

---

# UC-017 Record Expense

## Primary Actor

Finance Manager

## Description

Records business expenses.

## Preconditions

- Finance access granted.

## Main Flow

1. Add expense.
2. Enter amount.
3. Select category.
4. Save.

## Postconditions

- Expense recorded.

---

# UC-018 Generate Reports

## Primary Actor

Manager

## Description

Generates business reports.

## Preconditions

- Data available.

## Main Flow

1. Select report.
2. Choose date range.
3. Generate.
4. Export if required.

## Postconditions

- Report displayed.

---

# UC-019 View Dashboard

## Primary Actor

Business User

## Description

Displays KPIs and business insights.

## Preconditions

- User logged in.

## Main Flow

1. Login.
2. Dashboard loads.
3. View charts.
4. Filter data.

## Postconditions

- Dashboard displayed.

---

# UC-020 AI Sales Forecast

## Primary Actor

Business User

## Description

Predicts future sales using historical data.

## Preconditions

- Historical sales data exists.
- ML model deployed.

## Main Flow

1. Open AI Dashboard.
2. Select Sales Forecast.
3. Choose prediction period.
4. Run prediction.
5. Display forecast.

## Alternative Flow

- Insufficient historical data.
- Model unavailable.

## Postconditions

- Forecast displayed.

---

# UC-021 Inventory Demand Prediction

## Primary Actor

Inventory Manager

## Description

Predicts future inventory requirements.

## Preconditions

- Inventory history available.

## Main Flow

1. Select product.
2. Run prediction.
3. View recommended reorder quantity.

## Postconditions

- Demand forecast generated.

---

# UC-022 AI Assistant

## Primary Actor

Business User

## Description

Allows users to ask business-related questions using natural language.

## Preconditions

- User authenticated.

## Main Flow

1. Open AI Assistant.
2. Enter a question.
3. AI processes the request.
4. Response is displayed.

## Example Questions

- What were today's sales?
- Which products are low in stock?
- Show monthly revenue.
- Predict next month's sales.

## Postconditions

- AI-generated response displayed.

---

# UC-023 Export Reports

## Primary Actor

Manager

## Description

Exports reports for sharing or archival.

## Preconditions

- Report generated.

## Main Flow

1. Open report.
2. Select Export.
3. Choose PDF or Excel.
4. Download file.

## Postconditions

- Report exported successfully.

---

# UC-024 Manage User Roles

## Primary Actor

Organization Administrator

## Description

Assigns and updates user roles.

## Preconditions

- User account exists.

## Main Flow

1. Open User Management.
2. Select user.
3. Assign role.
4. Save.

## Postconditions

- User permissions updated.

---

# Summary

This document defines **24 primary use cases** covering:

- Authentication
- Organization Management
- HR Management
- Attendance
- Leave
- Payroll
- Inventory
- Warehouses
- Sales
- Customers
- Finance
- Reporting
- AI & Machine Learning
- AI Assistant
- User Management

These use cases provide the foundation for system design, implementation, testing, and user acceptance throughout the development of AetherERP AI.