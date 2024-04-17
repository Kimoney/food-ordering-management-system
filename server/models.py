from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-orders.user',)

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), unique= True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(100), unique= True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)


    orders = db.relationship('Order', backref='user')
# Association proxy
    foods = association_proxy('orders', 'food', creator=lambda food_obj: Order(food=food_obj))

    def __repr__(self):
        return f'<User: {self.id} {self.username}>'
    
    # this is a special property decorator for sqlalchemy
    # it leaves all of the sqlalchemy characteristics of the column in place
    @hybrid_property
    def password_hash(self):
        return self._password_hash

    # setter method for the password property
    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = self.simple_hash(password)

    # authentication method using user and password
    def authenticate(self, password):
        return self.simple_hash(password) == self._password_hash

    # simple_hash requires no access to the class or instance
    # let's leave it static
    @staticmethod
    def simple_hash(input):
        return sum(bytearray(input, encoding='utf-8'))

    
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