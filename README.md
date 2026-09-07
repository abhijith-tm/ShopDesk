# ShopDesk

ShopDesk is a shop management system I built as a learning project to understand how real-world backend and frontend applications are designed.

The project started as a small inventory management idea and evolved into a practical project where I learned a lot about Django, Django REST Framework, PostgreSQL, React, authentication, permissions, API design, database transactions, and frontend-backend integration.

## Tech Stack

### Backend

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT

### Frontend

- React
- Material UI
- Axios
- React Router

### Tools

- Git
- GitHub

## What ShopDesk Does

- Product and inventory management
- Sales management
- Sale cancellation and stock restoration
- Expense tracking
- User authentication
- User roles and permissions
- Business-level data isolation
- Protected frontend routes

## What I Built

### Products

- Product model
- Product CRUD API
- Database validation
- Stock management
- Business-level data isolation
- API tests

### Sales

- Sale and SaleItem models
- Historical product information stored with sales
- Sale creation service
- Stock validation
- Automatic stock deduction
- Database transactions
- Transaction rollback handling
- Sale cancellation
- Stock restoration after cancellation
- Sales history API
- Business-level data isolation

### Inventory

- Inventory adjustment model
- Stock adjustment tracking
- Adjustment reason and user tracking
- Business-level data isolation

### Expenses

- Expense model
- Expense API
- Expense tests

### Authentication & Authorization

- Custom user model
- Business creation during owner registration
- Owner registration
- JWT authentication
- Access and refresh token system
- HttpOnly refresh token cookie
- Current-user (`/me/`) API
- Django Groups for roles
- Owner, Manager and Employee roles
- Role-based API permissions
- Business-level data isolation

### Frontend

- React + Vite setup
- Material UI
- Login page
- Authentication context
- JWT access token management
- Axios API client
- Axios authentication interceptor
- Protected routes
- Current-user state
- Authentication restoration after page refresh
- Products page

## What I Learned

This project was mainly a learning experience. While building it, I learned:

- How Django projects and applications are structured
- Building REST APIs with Django REST Framework
- Designing database models and relationships
- PostgreSQL integration
- Serializers, views and permissions in DRF
- Service-layer patterns for business logic
- Database transactions with `transaction.atomic`
- Handling stock consistency during sales and cancellations
- JWT authentication
- Access vs refresh tokens
- HttpOnly cookies
- Role-based permissions
- Multi-business data isolation
- React state and Context API
- React Router and protected routes
- Axios interceptors
- Connecting a React frontend with a Django backend
- Testing backend business logic
- Debugging frontend/backend authentication issues
- Using Git and GitHub throughout development

## Project Structure

The project is split into a Django backend and React frontend.

```text
ShopDesk/
├── backend/
│   ├── authentication/
│   ├── products/
│   ├── sales/
│   ├── inventory/
│   ├── expenses/
│   └── config/
│
├── frontend/
│   └── src/
│       ├── API/
│       ├── authentication/
│       ├── pages/
│       └── ...
│
└── README.md
