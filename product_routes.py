from flask import Blueprint, request
from app.repositories.category_repo import CategoryRepository
from app.repositories.product_repo import ProductRepository
from app.services.product_service import ProductService

product_bp_v1 = Blueprint('product_v1', __name__, url_prefix='/api/v1/items')

category_repo = CategoryRepository()
product_repo = ProductRepository()
product_service = ProductService(product_repo, category_repo)

@product_bp_v1.route('', methods=['GET'])
def get_items():
    cat_query = request.args.get('category_id')
    min_price_query = request.args.get('min_price')
    return product_service.fetch_products(cat_query, min_price_query)

@product_bp_v1.route('/<int:item_id>', methods=['GET'])
def get_item(item_id):
    return product_service.get_product_by_id(item_id)

@product_bp_v1.route('', methods=['POST'])
def create_item():
    data = request.get_json(silent=True)
    return product_service.add_product(data)

@product_bp_v1.route('/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json(silent=True)
    return product_service.update_product(item_id, data)

@product_bp_v1.route('/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return product_service.delete_product(item_id)