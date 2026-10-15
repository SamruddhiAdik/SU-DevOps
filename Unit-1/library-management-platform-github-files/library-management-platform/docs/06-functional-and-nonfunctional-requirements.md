# Requirements Engineering Specification

## Functional requirements
- **FR-01 Authentication:** Role-based access for Admin, Librarian, Student, and Faculty.
- **FR-02 Book catalog management:** Create, read, update, and delete books, authors, categories, and shelf locations.
- **FR-03 Circulation engine:** Issue and return books while updating availability.
- **FR-04 Fine engine:** Calculate overdue penalties according to approved library rules and member tiers.
- **FR-05 Notification system:** Send due-date and overdue alerts.
- **FR-06 Search:** Search catalog entries by multiple fields.
- **FR-07 Reporting:** Provide inventory, circulation, overdue, and fine summaries.

## Non-functional requirements
- **NFR-01 Security:** Password hashing, secure sessions or tokens, HTTPS, and role-based authorization.
- **NFR-02 Performance:** Target sub-500 ms search API responses under the agreed concurrent load.
- **NFR-03 Availability and scalability:** Target 99.9% uptime in a production deployment with suitable scaling.
- **NFR-04 Maintainability:** Modular code, clear separation of concerns, and documented infrastructure.
- **NFR-05 Data integrity:** Enforce unique identifiers and consistent issue/return records.

## Validation note
These are requirements and targets from the assignment context. They have not been demonstrated under production load by this educational starter.
