from flask import Flask, make_response, jsonify, request, session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, User, Food, Order

app = Flask(__name__)
CORS(app)


app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.before_request
def check_if_logged_in():
    allowed_user_endpoints = ['indexuser', 'foodbyiduser', 'foodbyidcategoryuser', 'ordersuser', 'orderbyiduser', 'logout', 'checksession']
    allowed_admin_endpoints = ['indexadmin', 'foodbyidadmin', 'foodbyidcategoryadmin', 'allordersadmin', 'orderbyidadmin', 'logout', 'checksession']

    if session.get('user_id'):
        if session.get('user_role_admin') != True:
            if request.endpoint not in allowed_user_endpoints:
                return {'error': 'Unauthorized To Access This Resource'}, 401
        else:
            if request.endpoint not in allowed_admin_endpoints:
                return {'error': 'Unauthorized To Access This Resource'}, 401
    else:
        if request.endpoint not in ['checksession','logout', 'login', 'home', 'register']:
            return {'error': 'Unauthorized Log In First'}, 401

class MainHome(Resource):

    def get(self):
        resp = make_response({
            'project': 'Food Ordering Management System',
            'authors': ['John Kimani, Moses Letting, Dennis Kipkirui, Kelvin Kuria']
            }, 200)
        return resp

class Register(Resource):

    def post(self):

        data = request.get_json()
        if data:
            full_name = request.get_json()['full_name']
            username = request.get_json()['username']
            password = request.get_json()['password']

            new_user = User(full_name=full_name, username=username, password_hash=password)
            db.session.add(new_user)
            db.session.commit()
            resp = {'message': f'Congratulations {full_name}! Successfully Registered'}
            return make_response(resp, 201)
        else:
            return make_response({'message': 'All fields have to be filled'}, 401)
class CheckSession(Resource):

    def get(self):
        if session.get('user_id'):
            user = User.query.filter(User.id == session.get('user_id')).first()
            user_dict = {
                'id': user.id,
                'full_name': user.full_name,
                'username': user.username,
                'is_admin': user.is_admin,
            }
            return make_response(user_dict, 200)
        else:
            return {'message': '401: Not Authorized'}, 401
        
class Login(Resource):

    def post(self):
        
        data = request.get_json()
        if data:
            username = request.get_json()['username']
            user = User.query.filter(User.username == username).first()
            password = request.get_json()['password']
            
            if user:
                user.authenticate(password)
                print(user.authenticate(password))
                session['user_id'] = user.id
                session['user_role_admin'] = user.is_admin
                user_dict = {
                'id': user.id,
                'full_name': user.full_name,
                'username': user.username,
                'is_admin': user.is_admin,
            }
                return make_response(user_dict, 200)
            else:
                return make_response({'error': 'Invalid username or password'}, 401)

class Logout(Resource):

    def delete(self):
        session['user_id'] = None
        session['user_role_admin'] = None
        return {'message': '204: No Content'}, 204

 
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
        # Retrieve foods based on category
        foods = Food.query.filter_by(category=category).all()
        if not foods:
            return {'message': 'No foods found in this category'}, 404
        food_list = []
        for food in foods:
            food_data = {
                'id': food.id,
                'name': food.name,
                'category': food.category,
                'price': food.price,
                'description': food.description,
                'image': food.image
            }
            food_list.append(food_data)
        return {'foods': food_list}, 200

class OrdersUser(Resource):
    def get(self, id):
        # Retrieve orders placed by a single user
        orders = Order.query.filter_by(user_id=id).all()
        if not orders:
            return {'message': 'No orders found for this user'}, 404
        order_list = []
        for order in orders:
            order_data = {
                'id': order.id,
                'quantity': order.quantity,
                'time': order.time,
                'delivery_status': order.delivery_status,
                'user_id': order.user_id,
                'food_id': order.food_id
            }
            order_list.append(order_data)
        return make_response(jsonify({'orders': order_list}, 200))

# class OrderByIDUser(Resource):
#     # Orders a single user has placed
#     def get(self, user_id):
#         orders = Order.query.filter_by(user_id=user_id).order_by(Order.id.asc()).all()
#         orders_list = [{
#             'id': order.id,
#             'quantity': order.quantity,
#             'time': order.time,
#             'delivery_status': order.delivery_status,
#             'user_id': order.user_id,
#             'food_id': order.food_id
#         } for order in orders]
#         return make_response(jsonify({'orders': orders_list}), 200)

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
    def get(self, category):
        # Retrieve foods based on category
        foods = Food.query.filter_by(category=category).all()
        if not foods:
            return {'message': 'No foods found in this category'}, 404
        food_list = []
        for food in foods:
            food_data = {
                'id': food.id,
                'name': food.name,
                'category': food.category,
                'price': food.price,
                'description': food.description,
                'image': food.image
            }
            food_list.append(food_data)
        return {'foods': food_list}, 200

    def post(self, category):
        # Create a new food in the specified category
        data = request.form
        new_food = Food(
            name=data['name'],
            category=category,
            price=data['price'],
            description=data['description'],
            image=data['image']
        )
        db.session.add(new_food)
        db.session.commit()
        return {'message': 'Food created successfully', 'food': {
            'id': new_food.id,
            'name': new_food.name,
            'category': new_food.category,
            'price': new_food.price,
            'description': new_food.description,
            'image': new_food.image
        }}, 201

    def patch(self,food_id):
        # Update an existing food
        food = Food.query.get(food_id)
        if not food:
            return {'message': 'Food not found'}, 404

        data = request.form
        food.name = data.get('name', food.name)
        food.price = data.get('price', food.price)
        food.description = data.get('description', food.description)
        food.image = data.get('image', food.image)
        db.session.commit()
        return {'message': 'Food updated successfully', 'food': {
            'id': food.id,
            'name': food.name,
            'category': food.category,
            'price': food.price,
            'description': food.description,
            'image': food.image
        }}, 200

    def delete(self,food_id):
        # Delete a food
        food = Food.query.get(food_id)
        if not food:
            return {'message': 'Food not found'}, 404
        db.session.delete(food)
        db.session.commit()
        return {'message': 'Food deleted successfully'}, 200

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
            return make_response(jsonify({
                'id': order.id,
                'quantity': order.quantity,
                'time': order.time,
                'delivery_status': order.delivery_status,
                'user_id': order.user_id,
                'food_id': order.food_id
            }), 200)
        else:
            return make_response(jsonify({'message': 'Order not found'}), 404)

    def patch(self, id):
        order_to_update = Order.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(order_to_update, attr, request.form[attr])

        db.session.add(order_to_update)
        db.session.commit()

        return make_response(jsonify({
            'id': order_to_update.id,
            'quantity': order_to_update.quantity,
            'time': order_to_update.time,
            'delivery_status': order_to_update.delivery_status,
            'user_id': order_to_update.user_id,
            'food_id': order_to_update.food_id
        }), 200)

    def delete(self, id):
        order_to_delete = Order.query.filter_by(id=id).first()
        db.session.delete(order_to_delete)
        db.session.commit()
        return make_response(jsonify({'message': 'order successfully deleted'}), 200)


# Endpoints

api.add_resource(MainHome, '/', endpoint='home')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(CheckSession, '/check_session', endpoint='checksession')     
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(Register, '/register', endpoint='register')
api.add_resource(IndexUser, '/foods', endpoint='indexuser')
api.add_resource(FoodByIdUser, '/foods/<int:id>', endpoint='foodbyiduser')
api.add_resource(FoodByIdCategoryUser, '/foods/<string:category>', endpoint='foodbyidcategoryuser')
api.add_resource(OrdersUser, '/orders', endpoint='ordersuser')
# api.add_resource(OrderByIDUser, '/orders/<int:id>', endpoint='orderbyiduser')
api.add_resource(IndexAdmin, '/admin/foods', endpoint='indexadmin')
api.add_resource(FoodByIdAdmin, '/admin/foods/<int:id>', endpoint='foodbyidadmin')
api.add_resource(FoodByIdCategoryAdmin, '/admin/foods/<string:category>', endpoint='foodbyidcategoryadmin')
api.add_resource(AllOrdersAdmin, '/admin/orders', endpoint='allordersadmin')
api.add_resource(OrderByIdAdmin, '/admin/orders/<int:id>', endpoint='orderbyidadmin')


if __name__ == '__main__':
    app.run(port=5555, debug=True)