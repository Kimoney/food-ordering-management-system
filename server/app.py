from flask import Flask, make_response, jsonify, request, session
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)
from models import db, User, Food, Order

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
                return {'error': 'Unauthorized for 2this role'}, 401
        else:
            if request.endpoint not in allowed_admin_endpoints:
                return {'error': 'Unauthorized for 3this role'}, 401
    else:
        if request.endpoint not in ['checksession','logout', 'login', 'home', 'register']:
            return {'error': 'Unauthorized Log In First'}, 401

# Authentication
# Session Checker

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
# Log In
class Login(Resource):

    def post(self):
        
        data = request.get_json()
        if data:
            username = request.get_json()['username']
            user = User.query.filter(User.username == username).first()
            password = request.get_json()['password']
            
            if user:
                user.authenticate(password)
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

# Log Out
class Logout(Resource):

    def delete(self):
        session['user_id'] = None
        session['user_role_admin'] = None
        return {'message': '204: No Content'}, 204

 
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
                'description': food.description,
                'image': food.image,
            }
            foods.append(food_dict)
        resp = make_response(jsonify(foods), 200)
        return resp
     
class FoodByIdUser(Resource):
# View one food as the user
    def get(self, id):
        food = Food.query.filter(Food.id == id).first()
        food_dict = {
                'id':food.id,
                'name': food.name,
                'category': food.category,
                'price':food.price,
                'description': food.description,
                'image': food.image,
            }
        resp = make_response(jsonify(food_dict), 200)
        return resp

class FoodByIdCategoryUser(Resource):
# View several foods based on their category as the user
    def get(self, category):
        foods = []
        for food in Food.query.filter_by(category = category).all():
            food_dict = {
                'id':food.id,
                'name': food.name,
                'category': food.category,
                'price':food.price,
                'description': food.description,
                'image': food.image,
            }
            foods.append(food_dict)
        resp = make_response(jsonify(foods), 200)
        return resp

class OrdersUser(Resource):
# Orders a single user has placed
    def get(self):
        user_id = session.get('user_id')
        orders = []
        for order in Order.query.filter_by(user_id = user_id).all():
            print(Order.query.filter_by(user_id = user_id).all())
            order_dict = {
                'id': order.id,
                'delivery_status': order.delivery_status,
                'ordered_time': order.time,
                'food_id': order.food_id
            }
            orders.append(order_dict)
            print(orders)
        resp = make_response(orders, 200)
        return resp

class OrderByIDUser(Resource):
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
api.add_resource(OrderByIDUser, '/orders/<int:id>', endpoint='orderbyiduser')
api.add_resource(IndexAdmin, '/admin/foods', endpoint='indexadmin')
api.add_resource(FoodByIdAdmin, '/admin/foods/<int:id>', endpoint='foodbyidadmin')
api.add_resource(FoodByIdCategoryAdmin, '/admin/foods/<string:category>', endpoint='foodbyidcategoryadmin')
api.add_resource(AllOrdersAdmin, '/admin/orders', endpoint='allordersadmin')
api.add_resource(OrderByIdAdmin, '/admin/orders/<int:id>', endpoint='orderbyidadmin')


if __name__ == '__main__':
    app.run(port=5555, debug=True)