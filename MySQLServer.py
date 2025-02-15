import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Emirates1@"
        )

        # Ensure the connection was successful
        if connection.is_connected():
            cursor = connection.cursor()
            try:
                # Create the database if it doesn't exist
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as db_error:
                # Specifically catch errors that might occur when creating the database
                print(f"Failed to create database. Error: {db_error}")
            
    except Error as conn_error:
        # Handle any connection-related issues
        print(f"Failed to connect to MySQL server. Error: {conn_error}")
    
    finally:
        # Close the cursor and connection if they were opened
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Call the function to create the database
create_database()
