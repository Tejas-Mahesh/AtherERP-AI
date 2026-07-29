# Business Rules

## Authentication

- Every user must have a unique email address.
- Passwords must be securely encrypted.
- Users must authenticate before accessing the system.
- Role-based permissions must be enforced.

---

## Organization

- Each organization has its own isolated data.
- Users belong to one organization.
- Organizations cannot access each other's information.

---

## Employees

- Every employee must belong to one department.
- Employee IDs must be unique.
- Attendance can only be recorded once per day.
- Leave requests require approval.

---

## Inventory

- Products must belong to categories.
- Products are stored in warehouses.
- Stock cannot become negative.
- Every stock movement must be recorded.

---

## Suppliers

- Suppliers must have unique contact information.
- Suppliers can provide multiple products.

---

## Customers

- Customers may have multiple orders.
- Customer contact information must be unique.

---

## Sales

- Sales orders require customers.
- Invoices are generated automatically.
- Inventory updates after confirmed sales.

---

## Purchases

- Purchase orders require suppliers.
- Inventory increases after goods are received.

---

## Finance

- Payments reference invoices.
- Financial records cannot be deleted after approval.
- Audit logs must be maintained.

---

## Reporting

- Reports are generated using real-time data.
- Reports can be exported.

---

## Artificial Intelligence

- Predictions use historical business data.
- AI recommendations are advisory and do not modify business records automatically.