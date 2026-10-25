class CategoryRepository:
    def __init__(self):
        self.categories = [
            {"id": 1, "name": "Elektronik"},
            {"id": 2, "name": "Pakaian"}
        ]

    def get_all(self):
        return self.categories

    def get_by_id(self, category_id):
        return next((c for c in self.categories if c["id"] == category_id), None)

    def create(self, name):
        new_id = max([c["id"] for c in self.categories], default=0) + 1
        new_category = {"id": new_id, "name": name}
        self.categories.append(new_category)
        return new_category