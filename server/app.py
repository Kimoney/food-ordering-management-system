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
        try:
            foods = []
            for food in Food.query.all():
                foods.append({
                    'id': food.id,
                    'name': food.name,
                    'category': food.category,
                    'price': food.price,
                    'description': food.description,
                    'image': food.image
                })
            if foods:
                return make_response(jsonify({'message': 'success', 'data': foods}), 200)
            else:
                return make_response(jsonify({'message': 'No foods found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'An error occurred', 'error': str(e)}), 500)

class FoodByIdUser(Resource):
    # View one food as the user
    def get(self, id):
        food = Food.query.filter(Food.id == id).first()
        if food is None:
            return make_response(jsonify({'message': 'The requested food does not exist'}), 404)
        else:
            return make_response(jsonify({
                'id': food.id,
                'name': food.name,
                'category': food.category,
                'price': food.price,
                'description': food.description,
                'image': food.image
            }), 200)

class FoodByIdCategoryUser(Resource):
    # View several foods based on their category as the user
    def get(self, category):
        user = getattr(request, 'user', None)
        if not user:
            return {'error': 'Unauthorized'}, 401

        foods = Food.query.filter_by(category=category).all()
        user_orders = Order.query.filter_by(user_id=user.id).all()
        foods = [food for food in foods if any(order.food_id == food.id for order in user_orders)]
        foods_dict = [{
            'id': food.id,
            'name': food.name,
            'category': food.category,
            'price': food.price,
            'description': food.description,
            'image': food.image
        } for food in foods]
        return make_response(jsonify(foods_dict), 200)

class OrdersUser(Resource):
    # Orders a single user has placed
    pass

class OrderByIDUser(Resource):
    # Orders a single user has placed
    def get(self, user_id):
        orders = Order.query.filter_by(user_id=user_id).order_by(Order.id.asc()).all()
        orders_list = [{
            'id': order.id,
            'quantity': order.quantity,
            'time': order.time,
            'delivery_status': order.delivery_status,
            'user_id': order.user_id,
            'food_id': order.food_id
        } for order in orders]
        return make_response(jsonify({'orders': orders_list}), 200)

class IndexAdmin(Resource):
    # View All food as the Admin and perform all CRUD operations
    def get(self):
        food_list = [{
            'id': f.id,
            'name': f.name,
            'category': f.category,
            'price': f.price,
            'description': f.description,
            'image': f.image
        } for f in Food.query.all()]
        return make_response(jsonify(food_list), 200)

    def post(self):
        new_food = Food(
            name=request.form['name'],
            category=request.form['category'],
            price=request.form['price'],
            description=request.form['description'],
            image=request.form['image'],
        )
        db.session.add(new_food)
        db.session.commit()
        return make_response(jsonify({
            'id': new_food.id,
            'name': new_food.name,
            'category': new_food.category,
            'price': new_food.price,
            'description': new_food.description,
            'image': new_food.image
        }), 201)

class FoodByIdAdmin(Resource):
    # View one food as as the Admin and perform all CRUD operations
    def get(self, id):
        food = Food.query.filter_by(id=id).first()
        if food:
            return make_response(jsonify({
                'id': food.id,
                'name': food.name,
                'category': food.category,
                'price': food.price,
                'description': food.description,
                'image': food.image
            }), 200)
        else:
            return make_response(jsonify({'message': 'Food not found'}), 404)

    def patch(self, id):
        food_to_update = Food.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(food_to_update, attr, request.form[attr])

        db.session.commit()
        return make_response(jsonify({
            'id': food_to_update.id,
            'name': food_to_update.name,
            'category': food_to_update.category,
            'price': food_to_update.price,
            'description': food_to_update.description,
            'image': food_to_update.image
        }), 200)

    def delete(self, id):
        food_to_delete = Food.query.filter_by(id=id).first()
        db.session.delete(food_to_delete)
        db.session.commit()
        return make_response(jsonify({'message': 'Food successfully deleted'}), 200)

class FoodByIdCategoryAdmin(Resource):
    # View several foods based on their category as the Admin and handles all CRUD operations
    pass

class AllOrdersAdmin(Resource):
    # Shows all orders as the Admin and handles all CRUD operations
    def get(self):
        try:
            orders = [{
                'id': order.id,
                'quantity': order.quantity,
                'time': order.time,
                'delivery_status': order.delivery_status,
                'user_id': order.user_id,
                'food_id': order.food_id
            } for order in Order.query.all()]
            if orders:
                return make_response(jsonify({'message': 'success', 'data': orders}), 200)
            else:
                return make_response(jsonify({'message': 'No orders found'}), 404)
        except Exception as e:
            return make_response(jsonify({'message': 'An error occurred', 'error': str(e)}), 500)

    def post(self):
        new_order = Order(
            quantity=request.form['quantity'],
            delivery_status=request.form['delivery_status'],
            price=request.form['price'],
            user_id=request.form['user_id'],
            food_id=request.form['food_id'],
        )
        db.session.add(new_order)
        db.session.commit()
        return make_response({
            'id': new_order.id,
            'quantity': new_order.quantity,
            'time': new_order.time,
            'delivery_status': new_order.delivery_status,
            'user_id': new_order.user_id,
            'food_id': new_order.food_id
        }, 201)

class OrderByIdAdmin(Resource):
    # Show a single order as the Admin and handles all CRUD operations
    def get(self, id):
        order = Order.query.filter_by(id=id).first()
        if order:
            return jsonify({
                'id': order.id,
                'quantity': order.quantity,
                'time': order.time,
                'delivery_status': order.delivery_status,
                'user_id': order.user_id,
                'food_id': order.food_id
            }), 200
        else:
            return jsonify({'message': 'Order not found'}), 404

    def patch(self, id):
        order_to_update = Order.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(order_to_update, attr, request.form[attr])

        db.session.add(order_to_update)
        db.session.commit()

        return jsonify({
            'id': order_to_update.id,
            'quantity': order_to_update.quantity,
            'time': order_to_update.time,
            'delivery_status': order_to_update.delivery_status,
            'user_id': order_to_update.user_id,
            'food_id': order_to_update.food_id
        }), 200

    def delete(self, id):
        order_to_delete = Order.query.filter_by(id=id).first()
        db.session.delete(order_to_delete)
        db.session.commit()
        return jsonify({'message': 'order successfully deleted'}), 200

api.add_resource(IndexUser, '/foods')
api.add_resource(FoodByIdUser, '/foods/<int:id>')
api.add_resource(FoodByIdCategoryUser, '/foods/<string:category>')
api.add_resource(OrdersUser, '/orders')
api.add_resource(OrderByIDUser, '/orders/<int:id>')
api.add_resource(IndexAdmin, '/admin/foods')
api.add_resource(FoodByIdAdmin, '/admin/foods/<int:id>')
api.add_resource(FoodByIdCategoryAdmin, '/admin/foods/<string:category>')
api.add_resource(AllOrdersAdmin, '/admin/orders')
api.add_resource(OrderByIdAdmin, '/admin/orders/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)