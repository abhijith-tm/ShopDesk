# ShopDesk

ShopDesk is a shop management system I'm building to manage the day-to-day operations of a small shop.

The main goal of this project is to build something useful while learning how real-world backend applications are designed, tested, and deployed.

## Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- PostgreSQL

### Frontend
- React

### Tools
- Git
- GitHub

## What ShopDesk Will Do

The application will eventually provide:

- Product and inventory management
- Sales management
- Sale cancellation/refunds
- Expense tracking
- Dashboard
- Sales and profit reports
- Inventory reports
- User authentication and permissions

## Current Progress

### Products
- [x] Product model
- [x] Database validation and constraints
- [x] CRUD API
- [x] Tests

### Sales
- [x] Sale model
- [x] SaleItem model
- [x] Historical product snapshots
- [x] Sale serializers
- [x] Sale creation service
- [x] Stock validation
- [x] Stock deduction
- [x] Database transactions
- [x] Transaction rollback tests
- [ ] Sales API
- [ ] Sale cancellation/refund
- [ ] Sales history API

### Expenses
- [ ] Expense model
- [ ] Expense API
- [ ] Expense tests

### Dashboard & Reports
- [ ] Dashboard
- [ ] Sales reports
- [ ] Profit/loss reports
- [ ] Expense reports
- [ ] Inventory reports

### Frontend
- [x] React setup
- [x] Authentication
- [ ] Product management
- [ ] Sales/POS screen
- [ ] Sales history
- [ ] Expenses
- [ ] Dashboard
- [ ] Reports

### Deployment
- [ ] Docker
- [ ] AWS deployment
- [ ] CI/CD
- [ ] Production configuration

## Project Structure

The project is currently split into a Django backend and a React frontend.

```text
ShopDesk/
├── backend/
│   ├── products/
│   ├── sales/
│   └── ...
│
├── frontend/
│   └── ...
│
└── README.md
