# task_04_db.py
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# Function to read JSON data
def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return None

# Function to read CSV data
def read_csv():
    try:
        data = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price to float
                row['price'] = float(row['price'])
                row['id'] = int(row['id'])
                data.append(row)
        return data
    except Exception:
        return None

# Function to read SQLite data
def read_sql():
    if not os.path.exists('products.db'):
        return None
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]
        conn.close()
        return data
    except Exception:
        return None

@app.route('/products')
def products():
    source = request.args.get('source', 'json').lower()
    id_param = request.args.get('id')
    products_list = None
    error = None

    # Select data source
    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    elif source == 'sql':
        products_list = read_sql()
    else:
        error = "Wrong source"

    # Handle reading errors
    if products_list is None and error is None:
        error = "Error reading data"

    # Filter by ID if provided
    if products_list and id_param:
        try:
            id_int = int(id_param)
            products_list = [p for p in products_list if p['id'] == id_int]
            if not products_list:
                error = "Product not found"
        except ValueError:
            error = "Invalid id parameter"

    return render_template('product_display.html', products=products_list, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
