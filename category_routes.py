from flask import Blueprint, request
from app.repositories.category_repo import CategoryRepository
from app.services.category_service import CategoryService

category_bp_v1 = Blueprint('category_v1', __name__, url_prefix='/api/v1/categories')

category_repo = CategoryRepository()
category_service = CategoryService(category_repo)

@category_bp_v1.route('', methods=['GET'])
def get_categories():
    return category_service.fetch_all_categories()

@category_bp_v1.route('', methods=['POST'])
def create_category():
    data = request.get_json(silent=True)
    return category_service.add_category(data)