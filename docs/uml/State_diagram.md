# State Diagrams

**Project Name:** AetherERP AI

**Document ID:** UML-004

**Version:** 1.0

**Prepared By:** Tejas M

**Phase:** Day 4 - Database Design & UML Modeling

---

# 1. Introduction

## Purpose

This document defines the state transitions of important business entities in AetherERP AI.

State diagrams describe how objects move between different states during their lifecycle.

---

# 2. Invoice State Diagram

## Invoice Lifecycle
START

|

Draft

|

Generate Invoice

|

Created

|

Send Invoice

|

Sent

|

Payment Received?

    |
    |

YES | NO
|
|
Paid Pending Payment

|

Completed

|

END

NO

|

Reminder Sent

|

Waiting Payment


---

## Invoice States

| State | Description |
|---|---|
| Draft | Invoice created but not finalized |
| Created | Invoice generated |
| Sent | Sent to customer |
| Pending Payment | Waiting for payment |
| Paid | Payment completed |
| Completed | Transaction closed |

---

# 3. Sales Order State Diagram

## Order Lifecycle


START

|

Created

|

Confirmed

|

Processing

|

Inventory Check

Available?

  |
  |

YES | NO
|
|
Shipped Cancelled

|

Delivered

|

Completed

|

END


---

## Sales Order States

| State | Description |
|---|---|
| Created | Customer order placed |
| Confirmed | Order approved |
| Processing | Preparing order |
| Shipped | Product dispatched |
| Delivered | Customer received product |
| Completed | Order closed |
| Cancelled | Order stopped |

---

# 4. Purchase Order State Diagram

## Purchase Lifecycle


START

|

Draft

|

Submitted

|

Approval Required

|

Approved?

   |
   |

YES | NO
|
|
Ordered Rejected

|

Goods Received

|

Stock Updated

|

Completed

|

END


---

## Purchase States

| State | Description |
|---|---|
| Draft | Purchase request created |
| Submitted | Sent for approval |
| Approved | Purchase approved |
| Ordered | Supplier order created |
| Goods Received | Items received |
| Completed | Purchase finished |
| Rejected | Purchase denied |

---

# 5. Employee State Diagram

## Employee Lifecycle


START

|

Application Received

|

Interview Process

|

Selected?

   |
   |

YES | NO
|
|
Active Employee Rejected

|

On Probation

|

Permanent Employee

|

On Leave

|

Resigned

|

Inactive

|

END


---

## Employee States

| State | Description |
|---|---|
| Application Received | Candidate information stored |
| Active Employee | Working employee |
| Probation | Trial period |
| Permanent | Confirmed employee |
| On Leave | Temporarily unavailable |
| Resigned | Employee leaving |
| Inactive | No longer active |

---

# 6. Leave Request State Diagram

## Leave Workflow


START

|

Submitted

|

Manager Review

|

Decision

   |
   |

Approved Rejected

   |
   |

Processing

   |
   |

Completed

   |
   |

END


---

## Leave States

| State | Description |
|---|---|
| Submitted | Employee requested leave |
| Review | Waiting for approval |
| Approved | Leave accepted |
| Rejected | Leave denied |
| Completed | Leave period finished |

---

# 7. Inventory Stock State Diagram

## Stock Lifecycle


START

|

Product Created

|

Stock Added

|

Available

|

Stock Movement

    |
    |
| |
Stock In Stock Out
| |
Increase Decrease
| |
    |
    |

Quantity Check

Quantity = 0?

    |
    |

YES | NO
|
|
Out Of Stock Available


---

## Stock States

| State | Description |
|---|---|
| Available | Product ready for sale |
| Low Stock | Quantity below threshold |
| Out Of Stock | No inventory available |
| Discontinued | Product removed |

---

# 8. User Account State Diagram

## User Lifecycle


START

|

Registered

|

Email Verification

|

Active

|

Login

|

Authenticated

|

Account Locked?

    |
    |

YES | NO
|
|
Locked Continue Usage

|

Deactivated

|

END


---

## User States

| State | Description |
|---|---|
| Registered | Account created |
| Verified | Identity confirmed |
| Active | Can access system |
| Locked | Security restriction |
| Deactivated | Access removed |

---

# 9. AI Model State Diagram

## Machine Learning Model Lifecycle


START

|

Dataset Collection

|

Data Preparation

|

Training

|

Model Evaluation

Accuracy Good?

    |
    |

YES | NO
|
|
Deploy Retrain

|

Production Model

|

Prediction Generation

|

Model Monitoring

|

END


---

## AI Model States

| State | Description |
|---|---|
| Dataset Collection | Data gathered |
| Training | Model learning |
| Evaluation | Performance testing |
| Deployed | Available for prediction |
| Monitoring | Tracking performance |
| Retrain | Model improvement |

---

# 10. Notification State Diagram


START

|

Created

|

Queued

|

Sending

|

Delivered?

   |
   |

YES | NO
|
|
Read Failed

|

Archived

|

END


---

# 11. State Management Rules

The system must ensure:

- Invalid state changes are prevented
- Every transition is logged
- Approval actions require permission
- Important changes create audit records

---

# 12. Conclusion

State diagrams define lifecycle behavior in AetherERP AI.

They help developers implement:

- Status fields
- Approval workflows
- Business validations
- Automation rules
- Notification triggers

These diagrams complete the UML modeling phase before implementation.