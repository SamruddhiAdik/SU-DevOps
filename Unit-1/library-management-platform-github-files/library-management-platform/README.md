# Library Management Platform
**Unit 1: Product Engineering & Design Thinking**  
Training & Technical Project — Careertiq Training & Engineering Division

## Project overview
A proposed library platform to centralize book cataloging, membership, book issue/return, due dates, fine calculation, notifications, and administrative reporting.

## Core problem
Library members experience delays locating, reserving, borrowing, and returning resources because of manual tracking. Library staff need centralized inventory visibility and more reliable reporting.

## MVP scope
- Role-based access concept for Admin, Librarian, Student, and Faculty
- Book catalog and availability search
- Basic issue and return transactions
- Overdue fine calculation
- Basic administrative reports

## Repository structure
```text
library-management-platform/
├── .github/workflows/       # CI workflow
├── app/                     # Starter application and tests
│   ├── modules/             # Books, circulation, fines
│   ├── database/            # SQLite schema
│   └── tests/               # Automated tests
├── docs/                    # Requirements, personas, design thinking, architecture
├── docker/                  # Container setup
├── kubernetes/              # Example Kubernetes manifests
├── terraform/               # Infrastructure-as-code starter
├── ansible/                 # Configuration-management starter
├── monitoring/              # Monitoring notes/config starter
├── requirements.txt
└── README.md
```

## Run locally
Requires Python 3.10+.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python -m app.main
```
Open `http://127.0.0.1:5000`.

## API endpoints
- `GET /health`
- `GET /books`
- `POST /books`
- `POST /loans/issue`
- `POST /loans/return`
- `GET /reports/summary`

Example add-book JSON:
```json
{"title":"Clean Code","author":"Robert C. Martin","isbn":"9780132350884","category":"Software Engineering","shelf_location":"QA76.6"}
```

## Important scope and security note
This is an educational starter implementation, not a production-ready library system. Authentication/RBAC, password hashing, JWT, HTTPS, email/SMS, barcode/QR integrations, deployment automation, and production monitoring are documented as future implementation tasks and must be completed before real-world use.

## Assignment documents
See `docs/` for the business problem, design thinking stages, IBM Design Thinking/Loop, personas, stakeholder matrix, functional/non-functional requirements, product vision, MVP, roadmap, and architecture.
