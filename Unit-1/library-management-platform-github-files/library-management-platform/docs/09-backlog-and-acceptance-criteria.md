# Initial Product Backlog and Acceptance Criteria

| ID | User story | Priority | Acceptance criteria summary |
|---|---|---|---|
| US-01 | As a student, I want to search books so I can find relevant resources. | High | Search title/author/ISBN/category; show availability; handle no matches. |
| US-02 | As a librarian, I want to add a book so catalog inventory stays current. | High | Required fields validated; ISBN unique; saved book appears in catalog. |
| US-03 | As a librarian, I want to issue an available book so borrowing is recorded. | High | Book exists and is available; member is identified; due date is recorded; availability changes. |
| US-04 | As a librarian, I want to record a return so the copy becomes available. | High | Active loan exists; return date is recorded; availability changes; fine is calculated. |
| US-05 | As a librarian, I want overdue fines calculated so penalties follow policy. | Medium | Approved due date and fine rules are used; calculation is visible and testable. |
| US-06 | As an administrator, I want a summary report so I can monitor circulation. | Medium | Counts for books, available copies, active loans, and recorded fines are shown. |
| US-07 | As a member, I want due-date reminders so I can return books on time. | Medium | Reminder schedule and contact preferences are configured; delivery is logged. |
| US-08 | As an administrator, I want role-based permissions so sensitive actions are restricted. | High | Each role can perform only authorized actions; unauthorized requests are rejected. |

## Definition of Done
A backlog item is done when acceptance criteria pass, relevant automated/manual tests pass, code and documentation are reviewed, and security/privacy implications are considered.
