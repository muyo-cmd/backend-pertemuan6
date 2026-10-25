class ProductRepository:
    def __init__(self):
        self.products = [
            {"id": 1, "name": "Laptop Asus", "price": 8500000.0, "category_id": 1},
            {"id": 2, "name": "Mouse Wireless", "price": 150000.0, "category_id": 1}
        ]

    def get_all(self, category_id=None, min_price=None):
        result = self.products
        if category_id is not None:
            result = [p for p in result if p["category_id"] == category_id]
        if min_price is not None:
            result = [p for p in result if p["price"] >= min_price]
        return result

    def get_by_id(self, product_id):
        return next((p for p in self.products if p["id"] == product_id), None)

    def create(self, name, price, category_id):
        new_id = max([p["id"] for p in self.products], default=0) + 1
        new_product = {
            "id": new_id,
            "name": name,
            "price": float(price),
            "category_id": int(category_id)
        }
        self.products.append(new_product)
        return new_product

    def update(self, product_id, data):
        product = self.get_by_id(product_id)
        if not product:
            return None
        if "name" in data:
            product["name"] = data["name"]
        if "price" in data:
            product["price"] = float(data["price"])
        if "category_id" in data:
            product["category_id"] = int(data["category_id"])
        return product

    def delete(self, product_id):
        product = self.get_by_id(product_id)
        if not product:
            return False
        self.products = [p for p in self.products if p["id"] != product_id]
        return True