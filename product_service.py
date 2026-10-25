from app.utils.response_helper import success_response, fail_response

class ProductService:
    def __init__(self, product_repo, category_repo):
        self.product_repo = product_repo
        self.category_repo = category_repo

    def fetch_products(self, category_id_query=None, min_price_query=None):
        category_id = None
        min_price = None
        errors = {}

        if category_id_query is not None:
            try:
                category_id = int(category_id_query)
            except ValueError:
                errors["category_id"] = "Category ID harus berupa angka integer"

        if min_price_query is not None:
            try:
                min_price = float(min_price_query)
            except ValueError:
                errors["min_price"] = "Nilai min_price harus berupa angka"

        if errors:
            return fail_response(errors, code=400)

        products = self.product_repo.get_all(category_id, min_price)
        return success_response(data=products, code=200)

    def get_product_by_id(self, product_id):
        product = self.product_repo.get_by_id(product_id)
        if not product:
            return fail_response({"product": "Produk tidak ditemukan"}, code=404)
        return success_response(data=product, code=200)

    def add_product(self, data):
        if not data or not isinstance(data, dict):
            return fail_response({"body": "Harus berupa objek JSON yang valid"}, code=400)

        errors = {}

        if "name" not in data or not str(data["name"]).strip():
            errors["name"] = "Nama produk wajib diisi"

        if "price" not in data:
            errors["price"] = "Harga produk wajib diisi"
        else:
            try:
                price = float(data["price"])
                if price <= 0:
                    errors["price"] = "Harga harus lebih besar dari 0"
            except (ValueError, TypeError):
                errors["price"] = "Harga harus berupa angka"

        if "category_id" not in data:
            errors["category_id"] = "ID Pada Kategori Belum ditambahkan"
        else:
            cat = self.category_repo.get_by_id(data["category_id"])
            if not cat:
                errors["category_id"] = "ID Pada Kategori Belum ditambahkan"

        if errors:
            return fail_response(errors, code=400)

        created = self.product_repo.create(
            name=data["name"].strip(),
            price=float(data["price"]),
            category_id=int(data["category_id"])
        )
        return success_response(data=created, message="Item berhasil ditambahkan", code=201)

    def update_product(self, product_id, data):
        if not data or not isinstance(data, dict):
            return fail_response({"body": "Harus berupa objek JSON yang valid"}, code=400)

        existing = self.product_repo.get_by_id(product_id)
        if not existing:
            return fail_response({"product": "Produk tidak ditemukan"}, code=404)

        errors = {}
        if "price" in data:
            try:
                price = float(data["price"])
                if price <= 0:
                    errors["price"] = "Harga harus lebih besar dari 0"
            except (ValueError, TypeError):
                errors["price"] = "Harga harus berupa angka"

        if "category_id" in data:
            cat = self.category_repo.get_by_id(data["category_id"])
            if not cat:
                errors["category_id"] = "ID Pada Kategori Belum ditambahkan"

        if errors:
            return fail_response(errors, code=400)

        updated = self.product_repo.update(product_id, data)
        return success_response(data=updated, message="Item berhasil diperbarui", code=200)

    def delete_product(self, product_id):
        success = self.product_repo.delete(product_id)
        if not success:
            return fail_response({"product": "ID produk tidak ada"}, code=404)
        return success_response(message="Item berhasil dihapus", code=200)