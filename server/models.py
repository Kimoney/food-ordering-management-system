from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-orders.user',)

    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100), unique= True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    orders = db.relationship('Order', backref='user')
# Association proxy
    foods = association_proxy('orders', 'food', creator=lambda food_obj: Order(food=food_obj))
    
    def __repr__(self):
        return f'<User: {self.id} {self.username}>'
    
class Food(db.Model, SerializerMixin):
    __tablename__ = 'foods'
    serialize_rules = ('-orders.food',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)

    orders = db.relationship('Order', backref='food')

    users = association_proxy('orders', 'user', creator=lambda user_obj: Order(user=user_obj))

    def __repr__(self):
        return f'<Food: {self.id} {self.name} {self.price}>'
    
class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'
    serialize_rules = ('-order.users','-order.foods',)

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, server_default=db.func.now())
    delivery_status =db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'))

    def __repr__(self):
        return f'<Order: {self.id}  has {self.quantity} servings>'
    

# #assosciation table storing many to many relationship between food and user
# food_users=db.Table(
#     "food_users",
#     db.Column("food_id",db.Integer,db.ForeignKey("foods.id"),primary_key=True),
#     db.Column("user_id",db.Integer,db.ForeignKey("users.id"),primary_key=True),
# )

# #models
# class Food(db.Model,SerializerMixin):
#     __tablename__='foods'
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(100),nullable=False)
#     #relationship mapping food to related users
#     users=db.relationship(
#         "User",
#         secondary=food_users,
#         backref="foods"
#     )
#     def __repr__(self) -> str:
#         return f"Food {self.id} {self.name}"
    
    
# class User(db.Model,SerializerMixin):
#     __tablename__='users'
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(100),nullable=False)
#     contact=db.Column(db.Integer(10),nullable=False)
#     passowrd=db.Column(db.Integer(8),nullable=False)
#     #relationship mapping the users to related food
#     foods=db.relationship(
#         "Food",
#         secondary=food_users,
#         backref="users"
#     )
#     def __repr__(self) -> str:
#         return f"User {self.id} {self.name}"
    
# class Admin(db.Model,SerializerMixin):
#     __tablename__= 'admins'
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String,)
#     contact=db.Column(db.Integer(10),nullable=False)
#     food_id=db.Column(db.Integer,db.ForeignKey('foods.id'))
#     password=db.Column(db.Integer(8),nullable=False)
#     #relattionship mapping the admin to related food
#     food=db.relationship('Food',back_populate="admins")
#     def __repr__(self) -> str:
#         return f"Admin {self.id} {self.name} {self.contact} {self.password}"