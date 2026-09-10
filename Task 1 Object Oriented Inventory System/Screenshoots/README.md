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
Screenshots/
├── 01_Dashboard.png
├── 02_Add_Product.png
├── 03_Update_Product.png
├── 04_Remove_Product.png
├── 05_Search_Product.png
├── 06_Inventory_Records.png
├── 07_Validation_Test.png
└── 08_Data_Persistence.png
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


## 📈 Results

The system successfully provides a complete inventory management workflow through a Streamlit interface. Product information is stored persistently in JSON, while the dashboard provides useful inventory statistics such as total products, total quantity, categories, and overall inventory value.


## 👩‍💻 Developed By

**Wajeeha Tanveer**
Python Internship – Week 3
Aptura Tech Solutions

```
