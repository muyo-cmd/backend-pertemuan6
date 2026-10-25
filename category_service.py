from app.utils.response_helper import success_response, fail_response

class CategoryService:
    def __init__(self, category_repo):
        self.category_repo = category_repo

    def fetch_all_categories(self):
        categories = self.category_repo.get_all()
        return success_response(data=categories, code=200)

    def add_category(self, data):
        if not data or not isinstance(data, dict):
            return fail_response({"body": "Harus berupa objek JSON yang valid"}, code=400)

        errors = {}
        if "name" not in data or not str(data["name"]).strip():
            errors["name"] = "Nama kategori wajib diisi"

        if errors:
            return fail_response(errors, code=400)

        created = self.category_repo.create(data["name"].strip())
        return success_response(data=created, message="Kategori berhasil dibuat", code=201)