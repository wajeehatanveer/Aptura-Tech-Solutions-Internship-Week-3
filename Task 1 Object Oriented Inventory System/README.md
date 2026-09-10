````markdown
**Week 3 – Task 1**

# 📦 Object-Oriented Inventory System

A Python-based Inventory Management System developed using Object-Oriented Programming (OOP) principles and Streamlit. The application allows users to manage products, update stock information, search inventory, and monitor inventory performance through a user-friendly web interface.

## ✨ Features

- 📊 Inventory Dashboard with summary statistics
- ➕ Add new products
- ✎ Update existing product information
- 🗑️ Remove products
- 🔍 Search products by ID, name, or category
- 📋 View complete inventory records
- 💰 Calculate total value of each product
- 💾 Store inventory data persistently in JSON
- ✅ Input validation for products, prices, and quantities
- 🖥️ Interactive Streamlit web interface

## 🧩 OOP Implementation

The project uses Python classes to organize the inventory system:

- **Category** – Represents product categories.
- **Product** – Stores product details and provides update and total value functionality.
- **Inventory** – Handles inventory operations including adding, updating, removing, searching, saving, loading, and generating summaries.

## 🛠️ Technologies Used

- Python
- Streamlit
- JSON
- Object-Oriented Programming (OOP)

## 📁 Project Structure

```text
Task 1 - Object Oriented Inventory System/
│
├── app.py
├── inventory.py
├── inventory.json
└── README.md
````

## ▶️ How to Run

1. Install the required library:

```bash
pip install streamlit
```

2. Open the project folder in the terminal.

3. Run the application:

```bash
streamlit run app.py
```

## 🧪 Testing & Validation

The application was tested for the following operations:

* Adding a new product
* Preventing duplicate Product IDs
* Validating empty product fields
* Validating price and quantity values
* Updating existing products
* Removing products
* Searching products
* Displaying inventory records
* Calculating product-wise total value
* Saving and loading inventory data using JSON
* Displaying inventory summary statistics on the dashboard

## 📈 Results

The system successfully provides a complete inventory management workflow through a Streamlit interface. Product information is stored persistently in JSON, while the dashboard provides useful inventory statistics such as total products, total quantity, categories, and overall inventory value.


## 👩‍💻 Developed By

**Wajeeha Tanveer**
Python Internship – Week 3
Aptura Tech Solutions

```