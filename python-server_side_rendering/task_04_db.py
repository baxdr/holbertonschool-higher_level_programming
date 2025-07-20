from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def load_from_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except:
        return None


def load_from_csv():
    products = []
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except:
        return None


def load_from_sql():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except:
        return None


@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id')
    error = None
    data = None

    if source == 'json':
        data = load_from_json()
    elif source == 'csv':
        data = load_from_csv()
    elif source == 'sql':
        data = load_from_sql()
    else:
        error = "Wrong source"

    if data is None and error is None:
        error = "Failed to load data"

    filtered = []
    if not error:
        if id_param:
            try:
                target = int(id_param)
                filtered = [p for p in data if p.get('id') == target]
                if not filtered:
                    error = "Product not found"
            except:
                error = "Invalid id"
        else:
            filtered = data

    return render_template(
        'product_display.html',
        products=filtered,
        error=error,
        source=source
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
