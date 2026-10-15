"""Book catalog and circulation logic for the educational starter."""
from datetime import date
from app.database.db import get_connection

def add_book(data):
    with get_connection() as conn:
        try:
            cur = conn.execute(
                "INSERT INTO books(title, author, isbn, category, shelf_location) VALUES(?,?,?,?,?)",
                (data["title"].strip(), data["author"].strip(), data["isbn"].strip(),
                 data.get("category", "").strip(), data.get("shelf_location", "").strip()))
        except Exception as exc:
            if "UNIQUE constraint failed" in str(exc):
                raise ValueError("A book with this ISBN already exists.") from exc
            raise
        row = conn.execute("SELECT * FROM books WHERE id=?", (cur.lastrowid,)).fetchone()
        return dict(row)

def list_books(query=""):
    with get_connection() as conn:
        q = f"%{query.strip()}%"
        rows = conn.execute("""
            SELECT * FROM books
            WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ? OR category LIKE ?
            ORDER BY title
        """, (q, q, q, q)).fetchall()
        return [dict(row) for row in rows]

def issue_book(book_id, member_name):
    with get_connection() as conn:
        book = conn.execute("SELECT * FROM books WHERE id=?", (book_id,)).fetchone()
        if not book:
            raise LookupError("Book not found.")
        if not book["available"]:
            raise ValueError("Book is not currently available.")
        cur = conn.execute("INSERT INTO loans(book_id, member_name) VALUES(?,?)",
                           (book_id, member_name.strip()))
        conn.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
        row = conn.execute("SELECT * FROM loans WHERE id=?", (cur.lastrowid,)).fetchone()
        return dict(row)

def return_book(loan_id):
    with get_connection() as conn:
        loan = conn.execute("SELECT * FROM loans WHERE id=?", (loan_id,)).fetchone()
        if not loan:
            raise LookupError("Loan not found.")
        if loan["return_date"]:
            raise ValueError("This loan has already been returned.")
        today = date.today()
        due = date.fromisoformat(loan["due_date"])
        overdue_days = max((today - due).days, 0)
        # Educational example: fixed fine of 5 currency units per overdue day.
        fine = float(overdue_days * 5)
        conn.execute("UPDATE loans SET return_date=?, fine=? WHERE id=?",
                     (today.isoformat(), fine, loan_id))
        conn.execute("UPDATE books SET available=1 WHERE id=?", (loan["book_id"],))
        row = conn.execute("SELECT * FROM loans WHERE id=?", (loan_id,)).fetchone()
        return dict(row)

def summary():
    with get_connection() as conn:
        books = conn.execute("SELECT COUNT(*) FROM books").fetchone()[0]
        available = conn.execute("SELECT COUNT(*) FROM books WHERE available=1").fetchone()[0]
        active = conn.execute("SELECT COUNT(*) FROM loans WHERE return_date IS NULL").fetchone()[0]
        fines = conn.execute("SELECT COALESCE(SUM(fine),0) FROM loans").fetchone()[0]
        return {"total_books": books, "available_books": available,
                "active_loans": active, "fines_recorded": round(float(fines), 2)}
