# Activity Diagrams

**Project Name:** AetherERP AI

**Document ID:** UML-003

**Version:** 1.0

**Prepared By:** Tejas M

**Phase:** Day 4 - Database Design & UML Modeling

---

# 1. Introduction

## Purpose

This document defines the activity diagrams for important business workflows in AetherERP AI.

Activity diagrams represent:

- User actions
- System processes
- Decision points
- Data processing flow
- Completion states

---

# 2. User Login Activity Diagram

## Workflow
START

|

User Opens Login Page

|

Enter Username & Password

|

Submit Login Form

|

Validate Credentials

|

Is User Valid?

    |
    |

YES | NO
|
|
Create Session

    |
    |

Redirect Dashboard

    |
    |

END

NO

|

Show Error Message

|

Retry Login


---

# 3. Employee Creation Activity Diagram

## Workflow


START

|

HR Manager Opens Employee Module

|

Click Add Employee

|

Enter Employee Details

|

Validate Information

|

Is Data Valid?

    |
    |

YES | NO
|
|
Create Employee Record

    |
    |

Assign Department

    |
    |

Assign Role

    |
    |

Save Database

    |
    |

Send Notification

    |
    |

END

NO

|

Display Validation Error

|

Update Information


---

# 4. Sales Process Activity Diagram

## Workflow


START

|

Customer Selects Products

|

Create Sales Order

|

Check Inventory Availability

|

Stock Available?

    |
    |

YES | NO
|
|
Reserve Stock

    |
    |

Calculate Total Amount

    |
    |

Generate Invoice

    |
    |

Receive Payment

    |
    |

Update Inventory

    |
    |

Complete Sale

    |
    |

END

NO

|

Notify Product Unavailable

|

Suggest Alternative Product


---

# 5. Purchase Process Activity Diagram

## Workflow


START

|

Inventory Manager Checks Stock

|

Stock Low?

    |
    |

YES | NO
|
|
Create Purchase Request

    |
    |

Select Supplier

    |
    |

Create Purchase Order

    |
    |

Supplier Confirmation

    |
    |

Receive Products

    |
    |

Update Inventory

    |
    |

Complete Purchase

    |
    |

END

NO

|

Continue Monitoring Stock


---

# 6. Inventory Management Activity Diagram

## Workflow


START

|

Inventory Transaction Created

|

Identify Transaction Type

    |
    |
| |
Stock In Stock Out
| |
Increase Decrease
Quantity Quantity
| |
    |
    |

Update Stock Table

    |
    |

Generate Inventory Log

    |
    |

END


---

# 7. Leave Approval Activity Diagram

## Workflow


START

|

Employee Creates Leave Request

|

Submit Request

|

HR Manager Reviews Request

|

Approve or Reject?

    |
    |

APPROVE REJECT
| |
| |
Update Status Update Status

    |              |
    ----------------

            |

    Send Notification

            |

           END

---

# 8. Payroll Processing Activity Diagram

## Workflow


START

|

Payroll Manager Starts Process

|

Collect Employee Data

|

Calculate Salary

|

Apply Allowances

|

Apply Deductions

|

Generate Payslip

|

Save Payroll Record

|

Send Payslip

|

END


---

# 9. AI Prediction Activity Diagram

## Workflow


START

|

Collect Business Data

|

Extract Historical Records

|

Clean Data

|

Prepare Features

|

Load ML Model

|

Generate Prediction

|

Validate Result

|

Store Prediction

|

Display Dashboard Insight

|

END


---

# 10. Notification Activity Diagram

## Workflow


START

|

System Event Occurs

|

Create Notification

|

Select Notification Type

    |
    |

| |
Email In-App
| |
Send Message Store Alert

    |
    |

Update Notification Status

    |
    |

END


---

# 11. Common ERP Workflow Pattern


User Action

  |

Frontend Request

  |

Backend Validation

  |

Business Logic Processing

  |

Database Update

  |

Notification

  |

User Response


---

# 12. Activity Diagram Benefits

Activity diagrams help developers understand:

- Business workflows
- Decision points
- Validation rules
- Automation opportunities
- AI integration points

---

# 13. Conclusion

Activity diagrams define the operational workflows of AetherERP AI.
They provide a clear understanding of how users and system components perform business operations before implementation.