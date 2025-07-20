from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def load_from_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception:
        return None


def load_from_csv():
    products = []
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # cast types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception:
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
    else:
        error = "Wrong source"

    if data is None and error is None:
        error = "Failed to load data"

    # بعد تحميل البيانات بنفلتر حسب id إذا موجود
    filtered = []
    if not error:
        if id_param:
            try:
                target = int(id_param)
                filtered = [p for p in data if p.get('id') == target]
                if not filtered:
                    error = "Product not found"
            except ValueError:
                error = "Invalid id"
        else:
            filtered = data

    return render_template('product_display.html',
                           products=filtered,
                           error=error,
                           source=source)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
