from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, User, Food, Order

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/')
def index():
    resp = make_response({}, 200)
    return resp
class IndexUser(Resource):
# View all foods for the user's home/index page
     def get(self):
        foods = []
        for food in Food.query.all():
            food_dict = {
                'id':food.id,
                'name': food.name,
                'category': food.category,
                'price':food.price,
                'ingredients': food.ingredients
            }
            foods.append(food_dict)
        resp = make_response(jsonify(foods), 200)
        return resp
     
class FoodByIdUser(Resource):
# View one food as the user
    pass

class FoodByIdCategoryUser(Resource):
# View several foods based on their category as the user
    pass

class MyOrders(Resource):
# Orders a single user has placed
    pass

class IndexAdmin(Resource):
# View All food as the Admin and perform all CRUD operations
    pass

class FoodByIdAdmin(Resource):
# View one food as as the Admin and perform all CRUD operations
    pass

class FoodByIdCategoryAdmin(Resource):
# View several foods based on their category as the Admin and handles all CRUD operations
    pass

class AllOrdersAdmin(Resource):
# Shows all orders as the Admin and handles all CRUD operations
    pass

class OrderByIdAdmin(Resource):
# Shoe a single order as the Admin and handles all CRUD operations
    pass

     
api.add_resource(IndexUser, '/home')

if __name__ == '__main__':
    app.run(port=5555, debug=True)