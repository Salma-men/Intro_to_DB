import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL host
            user="username",       # Replace with your MySQL username
            password="putpasspowrdhere"        # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Print success message
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Print error message if connection or creation fails
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Run the function
create_database()