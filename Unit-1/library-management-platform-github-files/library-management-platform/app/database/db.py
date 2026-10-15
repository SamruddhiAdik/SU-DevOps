"""SQLite database setup for the educational starter."""
import os
import sqlite3

DB_PATH = os.environ.get("LIBRARY_DB_PATH", os.path.join(os.path.dirname(__file__), "library.db"))

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    with get_connection() as conn:
        conn.executescript("""
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
        """)
