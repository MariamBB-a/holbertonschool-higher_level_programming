from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

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
                # Convert id and price to proper types
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

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    json_file = os.path.join(os.path.dirname(__file__), 'products.json')
    csv_file = os.path.join(os.path.dirname(__file__), 'products.csv')

    data = []
    error_message = None

    # Determine source
    if source == 'json':
        data = read_json(json_file)
    elif source == 'csv':
        data = read_csv(csv_file)
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
