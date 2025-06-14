from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza

rp_bp = Blueprint(
    "restaurant_pizzas", __name__, url_prefix="/restaurant_pizzas"
)

@rp_bp.route("", methods=["POST"])
def create_rp():
    data = request.get_json()
    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get("restaurant_id")
    try:
        rp = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        db.session.add(rp)
        db.session.commit()
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
    return jsonify(rp.to_dict()), 201