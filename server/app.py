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
                food_dict = food.to_dict()
                foods.append(food_dict)
                
            if foods:
                return jsonify({'message':'success','data':foods}),200
            else:
                return jsonify({'message':'No foods found'}),404
        except Exception as e:
            return jsonify({'message':'An error occured', 'error':str(e)}),500
     
class FoodByIdUser(Resource):
# View one food as the user
    def get(self, id):
        food = Food.query.filter(Food.id == id).first()
        food_dict = food.to_dict()
        if food is None:
            return jsonify({'message':'The requested {food.id} does not exist'}),404
        else:
            return jsonify(food_dict),200

class FoodByIdCategoryUser(Resource):
# View several foods based on their category as the user
    def get(self, category):
        # Get the current user from the Flask request context
        user = getattr(request, 'user', None)
        if not user:
            return {'error': 'Unauthorized'}, 401

        # Get the category of food to view
        foods = Food.query.filter_by(category=category).all()

        # Filter the foods based on the user's orders
        user_orders = Order.query.filter_by(user_id=user.id).all()
        foods = [food for food in foods if any(order.food_id == food.id for order in user_orders)]
        # Convert the foods to a list of dictionaries
        foods_dict = [food.to_dict() for food in foods]
        return jsonify(foods_dict), 200

class OrdersUser(Resource):
# Orders a single user has placed
    pass

class OrderByIDUser(Resource):
# Orders a single user has placed
    pass

class IndexAdmin(Resource):
# View All food as the Admin and perform all CRUD operations
    def get(self):
        food_list=[f.to_dict() for f in Food.query.all()]
        return jsonify(food_list),200
    def post(self):
        new_food=Food(
            name=request.form['name'],
            category=request.form['category'],
            price=request.form['price'],
            description=request.form['description'],
            image=request.form['image'],
        )
        db.session.add(new_food)
        db.session.commit()
        return jsonify(new_food.to_dict()),201
class FoodByIdAdmin(Resource):
# View one food as as the Admin and perform all CRUD operations
    def get(self,id):
        food_dict=Food.query.filter_by(id=id).first().to_dict()
        return jsonify(food_dict),200
    def patch(self,id):
        food_to_update=Food.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(food_to_update,attr,request.form[attr])
            
        db.session.add(food_to_update)
        db.session.commit()
        return jsonify(food_to_update.to_dict()),200
    
    def delete(self,id):
        food_to_delete=Food.query.filter_by(id=id).first()
        db.session.delete(food_to_delete)
        db.session.commit()
        return jsonify({'message':'food successfully deleted'}),200

class FoodByIdCategoryAdmin(Resource):
# View several foods based on their category as the Admin and handles all CRUD operations
    pass

class AllOrdersAdmin(Resource):
# Shows all orders as the Admin and handles all CRUD operations
    def get(self):
        try:
            orders = []
            for order in Order.query.all():
                order_dict = order.to_dict()
                orders.append(order_dict)
                
            if orders:
                return jsonify({'message':'success','data':orders}),200
            else:
                return jsonify({'message':'No orders found'}),404
        except Exception as e:
            return jsonify({'message':'An error occured', 'error':str(e)}),500
        
    def post(self):
        new_order=Order(
            quantity=request.form['quantity'],
            delivery_status=request.form['delivery_status'],
            price=request.form['price'],
            user_id=request.form['user_id'],
            food_id=request.form['food_id'],
        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify(new_order.to_dict()),201

class OrderByIdAdmin(Resource):
# Show a single order as the Admin and handles all CRUD operations
    def get(self,id):
        order_dict=Order.query.filter_by(id=id).first().to_dict()
        return jsonify(order_dict),200
    def patch(self,id):
        order_to_update=Order.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(order_to_update,attr,request.form[attr])
            
        db.session.add(order_to_update)
        db.session.commit()
        return jsonify(order_to_update.to_dict()),200
    
    def delete(self,id):
        order_to_delete=Order.query.filter_by(id=id).first()
        db.session.delete(order_to_delete)
        db.session.commit()
        return jsonify({'message':'order successfully deleted'}),200

    
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