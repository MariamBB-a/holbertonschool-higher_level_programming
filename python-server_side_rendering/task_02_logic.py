from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    items_list = []
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
            # Ensure it is a list
            if not isinstance(items_list, list):
                items_list = []
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
