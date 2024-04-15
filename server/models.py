from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db=SQLAlchemy()

#assosciation table storing many to many relationship between food and user
food_users=db.Table(
    "food_users",
    db.Column("food_id",db.Integer,db.ForeignKey("foods.id"),primary_key=True),
    db.Column("user_id",db.Integer,db.ForeignKey("users.id"),primary_key=True),
)

#models
class Food(db.Model,SerializerMixin):
    __tablename__='foods'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    #relationship mapping food to related users
    users=db.relationship(
        "User",
        secondary=food_users,
        backref="foods"
    )
    def __repr__(self) -> str:
        return f"Food {self.id} {self.name}"
    
    
class User(db.Model,SerializerMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    contact=db.Column(db.Integer(10),nullable=False)
    passowrd=db.Column(db.Integer(8),nullable=False)
    #relationship mapping the users to related food
    foods=db.relationship(
        "Food",
        secondary=food_users,
        backref="users"
    )
    def __repr__(self) -> str:
        return f"User {self.id} {self.name}"
    
class Admin(db.Model,SerializerMixin):
    __tablename__= 'admins'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,)
    contact=db.Column(db.Integer(10),nullable=False)
    food_id=db.Column(db.Integer,db.ForeignKey('foods.id'))
    password=db.Column(db.Integer(8),nullable=False)
    #relattionship mapping the admin to related food
    food=db.relationship('Food',back_populate="admins")
    def __repr__(self) -> str:
        return f"Admin {self.id} {self.name} {self.contact} {self.password}"