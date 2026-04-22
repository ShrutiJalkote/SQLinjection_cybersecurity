# 🔐 SQL Injection Dashboard (Flask + MySQL)

A full-stack **cybersecurity mini project** that demonstrates **SQL Injection (SQLi) attacks** in a controlled environment.
This project allows users to simulate attacks, switch between vulnerable and secure modes, and monitor attack logs in real time.

---

## 🚀 Features

* 🔓 **Vulnerable Mode** – Demonstrates SQL Injection attacks
* 🔐 **Secure Mode** – Uses parameterized queries to prevent attacks
* 🎛 **Toggle Mode** – Switch between secure & vulnerable systems
* 📊 **Dashboard UI** – Clean interface using Bootstrap
* 🧪 **Live Attack Testing** – Try real SQL injection inputs
* 📁 **Attack Logs** – Stores and displays all inputs with timestamps

---

## 🧠 What is SQL Injection?

SQL Injection is a web security vulnerability that allows attackers to interfere with database queries.

### Example Attack:

```sql
1 OR 1=1
```

This modifies the query:

```sql
SELECT * FROM products WHERE id = 1 OR 1=1;
```

👉 Result: **All records are displayed (Unauthorized Access)**

---

## 🧩 Tech Stack

* **Frontend:** HTML, CSS, Bootstrap
* **Backend:** Python (Flask)
* **Database:** MySQL
* **Connector:** mysql-connector-python

---

## 📁 Project Structure

```
sqli-dashboard/
│── app.py
│── templates/
│     ├── dashboard.html
│     ├── logs.html
│── README.md
```

---

## 🗄️ Database Setup

### 1. Create Database

```sql
CREATE DATABASE sqli_dashboard;
USE sqli_dashboard;
```

### 2. Create Tables

#### Products Table

```sql
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price INT
);
```

#### Logs Table

```sql
CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    input VARCHAR(255),
    time DATETIME
);
```

### 3. Insert Sample Data

```sql
INSERT INTO products (name, price) VALUES
('Laptop', 60000),
('Mobile', 20000),
('Headphones', 3000);
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/sqli-dashboard.git
cd sqli-dashboard
```

### 2. Install Dependencies

```bash
pip install flask mysql-connector-python
```

### 3. Configure Database

Update `app.py`:

```python
database="sqli_dashboard"
password="YOUR_PASSWORD"
```

### 4. Run Application

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🧪 How to Test SQL Injection

### Normal Input:

```
1
```

### Attack Input:

```
1 OR 1=1
```

👉 In **Vulnerable Mode**:

* All products are displayed ❌

👉 In **Secure Mode**:

* Attack fails ✅

---

## 🔐 Security Implementation

### ❌ Vulnerable Query

```python
query = f"SELECT * FROM products WHERE id = {product_id}"
```

### ✅ Secure Query

```python
query = "SELECT * FROM products WHERE id = %s"
cursor.execute(query, (product_id,))
```

---

## 📊 Logs Feature

* Stores user input
* Tracks timestamp of each request
* Helps analyze attack patterns

---

## 🎯 Learning Outcomes

* Understand SQL Injection attacks
* Learn difference between vulnerable & secure systems
* Implement parameterized queries
* Build full-stack Flask applications

---

## 🚀 Future Enhancements

* 🔑 Login SQL Injection (Authentication bypass)
* 📈 Attack analytics using charts
* 🌐 Deploy on cloud (Render / Railway)
* 🧠 AI-based attack detection

---

## 📸 Screenshots

*Add your project screenshots here*

---

## 👩‍💻 Author

**Shruti Jalkote**
