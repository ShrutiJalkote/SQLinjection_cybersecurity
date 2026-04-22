from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import datetime

app = Flask(__name__)

SECURE_MODE = False  # Toggle manually or via UI

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shruti@06",
    database="sqli_dashboard"
)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    products = []
    logs = []

    if request.method == 'POST':
        product_id = request.form['product_id']
        cursor = db.cursor()

        # Toggle query
        if SECURE_MODE:
            query = "SELECT * FROM products WHERE id = %s"
            cursor.execute(query, (product_id,))
        else:
            query = f"SELECT * FROM products WHERE id = {product_id}"
            cursor.execute(query)

        products = cursor.fetchall()

        # Log attack
        log_query = "INSERT INTO logs (input, time) VALUES (%s, %s)"
        cursor.execute(log_query, (product_id, datetime.now()))
        db.commit()

    return render_template('dashboard.html', products=products, secure=SECURE_MODE)


@app.route('/toggle')
def toggle():
    global SECURE_MODE
    SECURE_MODE = not SECURE_MODE
    return redirect('/')


@app.route('/logs')
def view_logs():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY id DESC")
    logs = cursor.fetchall()
    return render_template('logs.html', logs=logs)


if __name__ == '__main__':
    app.run(debug=True)