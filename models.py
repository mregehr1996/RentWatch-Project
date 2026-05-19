
from app.database import get_connection


class RentalReport:

    @staticmethod
    def create(apartment_name, city, state, rent_price, rating, review):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO rental_reports
        (apartment_name, city, state, rent_price, rating, review)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            apartment_name,
            city,
            state,
            rent_price,
            rating,
            review
        ))

        connection.commit()
        connection.close()

    @staticmethod
    def get_all():
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT * FROM rental_reports
        ORDER BY created_at DESC
        """)

        reports = cursor.fetchall()

        connection.close()

        return reports

    @staticmethod
    def search(city=None, apartment_name=None):
        connection = get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM rental_reports WHERE 1=1"
        params = []

        if city:
            query += " AND city LIKE ?"
            params.append(f"%{city}%")

        if apartment_name:
            query += " AND apartment_name LIKE ?"
            params.append(f"%{apartment_name}%")

        query += " ORDER BY created_at DESC"

        cursor.execute(query, params)

        reports = cursor.fetchall()

        connection.close()

        return reports
