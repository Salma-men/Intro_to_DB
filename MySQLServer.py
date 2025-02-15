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
        
        # Check if the connection was successful
        if connection.is_connected():
            cursor = connection.cursor()
            try:
                # Create the database if it doesn't already exist
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as db_error:
                # Handle errors related to database creation
                print(f"Error while creating database: {db_error}")
            
    except Error as e:
        # Handle connection errors
        print(f"Error: {e}")
    
    finally:
        # Ensure resources are closed
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Call the function to create the database
create_database()