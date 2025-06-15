from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

# Seed restaurants
r1 = Restaurant(name="Pizza Palace", address="123 Main St")
r2 = Restaurant(name="Kiki's Pizza", address="456 Elm St")
db.session.add_all([r1, r2])

# Seed pizzas
p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
db.session.add_all([p1, p2])
db.session.commit()

# Link pizzas to restaurants
rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
rp2 = RestaurantPizza(price=12, restaurant_id=r2.id, pizza_id=p2.id)
db.session.add_all([rp1, rp2])
db.session.commit()

print("Seed data inserted")