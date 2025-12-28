# Clean Architecture User Management with TDD (Python)

## 📌 Project Overview
This project is a **didactic implementation of Clean Architecture** using **Python** and **Test Driven Development (TDD)**.

The objective of this project is to demonstrate how to build a maintainable and testable software system by strictly applying:
- Clean Architecture principles
- SOLID principles
- Test Driven Development (RED / GREEN / BLUE)
- Separation of concerns

The project implements a simple **User creation use case**, developed step by step exactly as taught in class.

---

## 🧱 Architecture

The project follows **Clean Architecture**, where dependencies always point **inward** toward the business logic.

External Systems
│
├── API (FastAPI)
│ └── Controller
│
├── Presenter
│ └── ViewModel
│
├── Use Cases (Business Logic)
│ └── SavingUserUseCase
│
├── Entities
│ └── User
│
└── Infrastructure
└── MySQL Repository

### Architectural Rules Applied
- Business logic does **not** depend on frameworks
- Controllers contain no business logic
- Repositories are accessed only through interfaces
- Presenters handle output formatting
- Entities are pure and framework-independent

---

## 🧪 Test Driven Development (TDD)

The entire project was built using **TDD**.

### 🔴 RED
- Write a failing test
- Define behavior before implementation

### 🟢 GREEN
- Write the minimum code to make the test pass

### 🔵 BLUE
- Refactor the code
- Improve structure and readability
- Keep all tests passing

Each layer (Use Case, Presenter, Controller, API) was introduced incrementally following this cycle.

---

## 📂 Project Structure

src/
├── entities/
│ └── user.py
│
├── repositories/
│ └── user_repository_interface.py
│
├── use_cases/
│ └── saving_use_case.py
│
├── presenters/
│ └── user_presenter.py
│
├── controllers/
│ └── saving_user_controller.py
│
├── view_models/
│ └── user_view_model.py
│
├── infrastructure/
│ └── mysql_user_repository.py
│
└── main.py
tests/
├── use_cases/
├── controllers/
└── api/

---

## 🚀 API Example (FastAPI)

### Endpoint
```http
POST /users
Request Body
{
  "first_name": "Abdelhakim",
  "last_name": "Berrim"
}
Response
{
  "full_name": "Abdelhakim Berrim"
}

🧠 Business Rules

The following business rules were implemented:

A user must have a first name and last name

The user entity is saved using a repository abstraction

The use case delegates persistence to the repository

The presenter is always called after the use case execution

The API never exposes domain entities directly

All business rules are located exclusively inside the Use Case layer.

🛠 Technologies Used

Python

Pytest

unittest.mock

FastAPI

MySQL (Infrastructure layer simulation)

🎯 Educational Purpose

This project was created for academic purposes to validate understanding of:

Clean Architecture

TDD methodology

Dependency Inversion Principle

Maintainable software design

The business logic is intentionally simple in order to focus on architecture quality and testability.

👤 Author

Abdelhakim Berrim

✅ Final Notes

This project demonstrates that:

Architecture matters more than frameworks

Tests drive design

Business logic can be developed independently from infrastructure

Additional business rules or external systems can be added easily without breaking the existing structure.
