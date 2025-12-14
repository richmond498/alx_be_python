#!/usr/bin/env python3
"""
Creates the database `alx_book_store` on a MySQL server.
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error


def create_database():
    connection = None
    cursor = None
    try:
        # Update these credentials as needed
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )

        cursor = connection.cursor()

        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection
        if cursor is not None:
            try:
                cursor.close()
            except Error:
                pass
        if connection is not None and connection.is_connected():
            try:
                connection.close()
            except Error:
                pass


if __name__ == "__main__":
    create_database()
