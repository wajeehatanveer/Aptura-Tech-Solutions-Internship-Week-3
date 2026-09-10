import json
import os


class Category:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            "name": self.name
        }


class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def update(self, name=None, category=None, price=None, quantity=None):
        if name is not None:
            self.name = name

        if category is not None:
            self.category = category

        if price is not None:
            self.price = price

        if quantity is not None:
            self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }


class Inventory:
    def __init__(self, file_name="inventory.json"):
        self.file_name = file_name
        self.products = []
        self.load_data()

    def add_product(self, product):
            
        # Validate Product ID
        if not product.product_id.strip():
            return False, "Product ID cannot be empty."

        # Check duplicate Product ID
        if any(p.product_id == product.product_id for p in self.products):
            return False, "Product ID already exists."

        # Validate Product Name
        if not product.name.strip():
            return False, "Product name cannot be empty."

        # Validate Category
        if not product.category.strip():
            return False, "Category cannot be empty."

        # Validate Price
        if product.price <= 0:
            return False, "Price must be greater than 0."

        # Validate Quantity
        if product.quantity < 0:
            return False, "Quantity cannot be negative."

        # Add product
        self.products.append(product)

        # Save inventory
        self.save_data()

        return True, "Product added successfully."
        

    def update_product(self, product_id, **kwargs):
        for product in self.products:
            if product.product_id == product_id:

                if "name" in kwargs:
                    if not kwargs["name"].strip():
                        return False, "Product name cannot be empty."

                if "category" in kwargs:
                    if not kwargs["category"].strip():
                        return False, "Category cannot be empty."

                if "price" in kwargs:
                    if kwargs["price"] <= 0:
                        return False, "Price must be greater than 0."

                if "quantity" in kwargs:
                    if kwargs["quantity"] < 0:
                        return False, "Quantity cannot be negative."

                product.update(**kwargs)
                self.save_data()

                return True, "Product updated successfully."

        return False, "Product not found."
        

    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                self.save_data()

                return True, "Product removed successfully."

        return False, "Product not found."


    def search_product(self, keyword):
        keyword = keyword.strip().lower()

        if not keyword:
            return []

        results = []

        for product in self.products:
            if (
                keyword in product.product_id.lower()
                or keyword in product.name.lower()
                or keyword in product.category.lower()
            ):
                results.append(product)

        return results

    def get_all_products(self):
        return self.products

    def save_data(self):
        data = [product.to_dict() for product in self.products]

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if not os.path.exists(self.file_name):
            return

        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)

            for item in data:
                product = Product(
                    item["product_id"],
                    item["name"],
                    item["category"],
                    item["price"],
                    item["quantity"]
                )

                self.products.append(product)

        except (json.JSONDecodeError, KeyError):
            self.products = []

    def get_summary(self):
        total_products = len(self.products)

        total_quantity = sum(
            product.quantity for product in self.products
        )

        total_value = sum(
            product.total_value() for product in self.products
        )

        categories = set(
            product.category for product in self.products
        )

        low_stock_products = sum(
            1 for product in self.products
            if product.quantity <= 5
        )

        return {
            "total_products": total_products,
            "total_quantity": total_quantity,
            "total_value": total_value,
            "total_categories": len(categories),
            "low_stock_products": low_stock_products
        }
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    inventory = Inventory()

    product = Product(
        "P0012",
        "mobile",
        "Electronics",
        65000,
        2
    )

    success, message = inventory.add_product(product)
    print(message)

    print("\nAll Products:")
    for product in inventory.get_all_products():
        print(product.to_dict())

    print("\nSummary:")
    print(inventory.get_summary())

    print("\nSearch Result:")
    results = inventory.search_product("Laptop")

    for product in results:
        print(product.to_dict())       