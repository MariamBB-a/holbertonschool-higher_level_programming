import sqlite3
import os

def create_database():
    # Remove existing database if it exists
    if os.path.exists('products.db'):
        os.remove('products.db')

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Create Products table
    cursor.execute('''
        CREATE TABLE Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insert sample data
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    conn.commit()
    conn.close()
    print("Database created successfully.")

if __name__ == '__main__':
    create_database()
