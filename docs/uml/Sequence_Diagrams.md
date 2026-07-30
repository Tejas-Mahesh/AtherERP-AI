# Sequence Diagrams

Project Name: AetherERP AI

Document ID: UML-002

Version: 1.0

Prepared By: Tejas M

Phase: Day 4 - Database Design & UML Modeling

---

# 1. Introduction

## Purpose

This document defines the interaction flow between users, frontend, backend services, database, and AI services.

Sequence diagrams explain how system components communicate during important operations.

---

# 2. User Login Sequence Diagram

## Flow

User logs into the ERP system.
User

|

| Enter Username & Password

|

Frontend

|

| Send Login Request

|

Authentication Service

|

| Verify Credentials

|

Database

|

| Return User Data

|

Authentication Service

|

| Generate Session

|

Frontend

|

| Display Dashboard

|

User


---

## Components

- User
- Frontend
- Authentication Service
- Database
- Session Manager

---

# 3. Employee Creation Sequence Diagram

## Flow

HR Manager creates a new employee.
HR Manager

|

| Submit Employee Details

|

Frontend

|

| Send Request

|

Employee Service

|

| Validate Data

|

Database

|

| Save Employee

|

Employee Service

|

| Return Success

|

Frontend

|

Display Confirmation


---

## Components

- HR Manager
- Frontend
- Employee Service
- Database

---

# 4. Sales Order Sequence Diagram

## Flow

Customer purchase process.
Customer

|

Create Order

|

Sales Module

|

Check Product Availability

|

Inventory Service

|

Query Stock

|

Database

|

Return Stock Status

|

Sales Module

|

Create Sales Order

|

Database

|

Generate Invoice

|

Invoice Service

|

Send Confirmation

|

Customer


---

## Components

- Customer
- Sales Service
- Inventory Service
- Invoice Service
- Database

---

# 5. Purchase Order Sequence Diagram

## Flow

Company purchases products from supplier.
Inventory Manager

|

Create Purchase Request

|

Purchase Module

|

Select Supplier

|

Supplier Service

|

Create Purchase Order

|

Database

|

Save Order

|

Supplier

|

Confirm Delivery

|

Inventory Service

|

Update Stock

|

Database


---

## Components

- Inventory Manager
- Purchase Service
- Supplier Service
- Inventory Service
- Database

---

# 6. Inventory Update Sequence Diagram

## Flow

Stock changes after purchase or sale.


Sales/Purchase Module

|

Stock Update Request

|

Inventory Service

|

Validate Product

|

Database

|

Update Quantity

|

Database

|

Save Transaction

|

Inventory Service

|

Return Updated Stock


---

## Components

- Sales Module
- Purchase Module
- Inventory Service
- Database

---

# 7. AI Prediction Sequence Diagram

## Flow

Business data is used for prediction.


Business Data

|

Data Collection Service

|

Database

|

Extract Historical Data

|

AI Processing Service

|

Data Cleaning

|

Feature Engineering

|

ML Model

|

Generate Prediction

|

Prediction Database

|

Store Result

|

Dashboard

|

Display Insight


---

## Components

- Database
- Data Pipeline
- AI Service
- ML Model
- Dashboard

---

# 8. Notification Sequence Diagram

## Flow

System sends alerts.


System Event

|

Notification Service

|

Create Notification

|

Database

|

Store Message

|

Email/SMS Service

|

Send Notification

|

User


---

# 9. General System Communication Pattern


User

↓

Frontend

↓

API Layer

↓

Service Layer

↓

Repository Layer

↓

Database

AI Requests:

Service Layer

↓

AI Engine

↓

Prediction Storage

↓

Dashboard


---

# 10. Conclusion

Sequence diagrams define the runtime behavior of AetherERP AI.

They help developers understand:

- Request flow
- Service communication
- Database interaction
- AI processing workflow

These diagrams will guide backend API and service implementation.