"""Educational Library Management Platform API starter."""
from flask import Flask, jsonify, request
from app.database.db import init_db, get_connection
from app.modules.library import add_book, list_books, issue_book, return_book, summary

def create_app():
    app = Flask(__name__)
    init_db()

    @app.get("/health")
    def health():
        return jsonify({"status": "ok", "service": "library-management-platform"})

    @app.get("/books")
    def books():
        return jsonify(list_books(request.args.get("q", "")))

    @app.post("/books")
    def create_book():
        data = request.get_json(silent=True) or {}
        required = ["title", "author", "isbn"]
        missing = [key for key in required if not str(data.get(key, "")).strip()]
        if missing:
            return jsonify({"error": "Missing required fields", "fields": missing}), 400
        try:
            book = add_book(data)
            return jsonify(book), 201
        except ValueError as exc:
            return jsonify({"error": str(exc)}), 409

    @app.post("/loans/issue")
    def issue():
        data = request.get_json(silent=True) or {}
        if not data.get("book_id") or not data.get("member_name"):
            return jsonify({"error": "book_id and member_name are required"}), 400
        try:
            return jsonify(issue_book(int(data["book_id"]), data["member_name"])), 201
        except (ValueError, LookupError) as exc:
            return jsonify({"error": str(exc)}), 400

    @app.post("/loans/return")
    def return_loan():
        data = request.get_json(silent=True) or {}
        if not data.get("loan_id"):
            return jsonify({"error": "loan_id is required"}), 400
        try:
            return jsonify(return_book(int(data["loan_id"]))), 200
        except (ValueError, LookupError) as exc:
            return jsonify({"error": str(exc)}), 400

    @app.get("/reports/summary")
    def reports():
        return jsonify(summary())

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
