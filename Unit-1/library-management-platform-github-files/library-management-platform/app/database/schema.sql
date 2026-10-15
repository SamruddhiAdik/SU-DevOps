CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT NOT NULL UNIQUE,
    category TEXT DEFAULT '',
    shelf_location TEXT DEFAULT '',
    available INTEGER NOT NULL DEFAULT 1 CHECK (available IN (0,1))
);
CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL REFERENCES books(id),
    member_name TEXT NOT NULL,
    issue_date TEXT NOT NULL DEFAULT (date('now')),
    due_date TEXT NOT NULL DEFAULT (date('now', '+14 days')),
    return_date TEXT,
    fine REAL NOT NULL DEFAULT 0
);
