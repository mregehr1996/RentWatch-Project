
import sqlite3

DATABASE_NAME = "rentwatch.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rental_reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        apartment_name TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        rent_price REAL NOT NULL,
        rating INTEGER NOT NULL,
        review TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    connection.commit()
    connection.close()
