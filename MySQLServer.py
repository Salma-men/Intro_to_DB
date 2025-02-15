import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (update with your credentials)
        connection = mysql.connector.connect(
            host='localhost',  # Change if necessary
            user='root',       # Change if necessary
            password='Emirates1@'  # Replace with your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()