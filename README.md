# Pizza Restaurant API

## Overview

-This is a RESTful API for managing Pizza Restaurants, built with Flask. It uses SQLAlchemy for ORM and follows the MVC (Model–View–Controller) design pattern.

## Project Structure

```bash
server/
├── __init__.py
├── app.py              # Flask app setup
├── config.py           # Database configuration
├── models/             # SQLAlchemy models
│   ├── __init__.py
│   ├── restaurant.py
│   ├── pizza.py
│   └── restaurant_pizza.py
├── controllers/        # Route controllers
│   ├── __init__.py
│   ├── restaurant_controller.py
│   ├── pizza_controller.py
│   └── restaurant_pizza_controller.py
└── seed.py             # Database seeding script

migrations/              # Flask-Migrate scripts
challenge-1-pizzas.postman_collection.json
README.md
```


## Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/your-username/pizza-api-challenge.git
cd pizza-api-challenge
```

2. Create and Activate a Virtual Environment

```bash
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
```

3. Set Up the Database

```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

4. Seed the Database

```bash
python server/seed.py
```


## Models and Validations

### Restaurant

id: Integer, Primary Key

name: String

address: String

Relationships: has many RestaurantPizzas

### Pizza

id: Integer, Primary Key

name: String

ingredients: String

Relationships: has many RestaurantPizzas

### RestaurantPizza (Join Table)

id: Integer, Primary Key

price: Integer (Validation: must be between 1 and 30)

restaurant_id: Foreign Key → Restaurant

pizza_id: Foreign Key → Pizza

Relationships: belongs to Restaurant and Pizza

Cascading deletes: Deleting a restaurant deletes associated RestaurantPizzas

## Routes Summary

### GET /restaurants

Returns a list of all restaurants.

### GET /restaurants/

Returns one restaurant and its pizzas.

404: { "error": "Restaurant not found" }

### DELETE /restaurants/

Deletes a restaurant and all associated RestaurantPizzas.

204 No Content on success

404: { "error": "Restaurant not found" }

### GET /pizzas

Returns a list of all pizzas.

### POST /restaurant_pizzas

Creates a RestaurantPizza.

Request Body:

```bash
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

Success Response:

```bash
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Emma",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "address2"
  }
}
```

Error Response (400):

```bash
{ "errors": ["Price must be between 1 and 30"] }
```

## Testing with Postman

Open Postman

Click Import → Upload challenge-1-pizzas.postman_collection.json

Use the defined requests to test:

-List restaurants

-Get restaurant by ID

-Delete restaurant

-List pizzas

-Create a restaurant pizza

