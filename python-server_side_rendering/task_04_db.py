from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# ----- Helper Functions -----
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_csv(file_path):
    products = []
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row['id'] = int(row.get('id', 0))
                    row['price'] = float(row.get('price', 0))
                except ValueError:
                    row['id'] = 0
                    row['price'] = 0.0
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products

def read_sqlite(db_path):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except Exception as e:
        print(f"Error reading SQLite: {e}")
    return products

# ----- Flask Route -----
@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    base_path = os.path.dirname(__file__)
    json_file = os.path.join(base_path, 'products.json')
    csv_file = os.path.join(base_path, 'products.csv')
    db_file = os.path.join(base_path, 'products.db')

    data = []
    error_message = None

    # Select source
    if source == 'json':
        data = read_json(json_file)
    elif source == 'csv':
        data = read_csv(csv_file)
    elif source == 'sql':
        data = read_sqlite(db_file)
    else:
        error_message = "Wrong source"
        data = []

    # Filter by id if provided
    if id_param and error_message is None:
        try:
            id_int = int(id_param)
            filtered = [item for item in data if item.get('id') == id_int]
            if not filtered:
                error_message = "Product not found"
            else:
                data = filtered
        except ValueError:
            error_message = "Invalid id parameter"

    return render_template('product_display.html', products=data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
