#!/usr/bin/env python3
"""
MySQLServer.py
Script to create the database 'alx_book_store' in MySQL.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # 👈 change this to your MySQL username
            password="Mokone"   # 👈 change this to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            # Optional: print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
