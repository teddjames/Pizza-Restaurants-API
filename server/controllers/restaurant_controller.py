from flask import Blueprint, jsonify
from server.app import db
from server.models.restaurant import Restaurant

restaurant_bp = Blueprint(
    "restaurants", __name__, url_prefix="/restaurants"
)

@restaurant_bp.route("", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants])

@restaurant_bp.route("/<int:id>", methods=["GET"])
def get_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify({"error": "Restaurant not found"}), 404
    data = r.to_dict()
    data["pizzas"] = [rp.to_dict() for rp in r.pizzas]
    return jsonify(data)

@restaurant_bp.route("/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(r)
    db.session.commit()
    return "", 204