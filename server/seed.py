from models import db, User, Food, Order
from app import app
from faker import Faker
from faker_food import FoodProvider

fake = Faker()
fake.add_provider(FoodProvider)

img = 'https://images.pexels.com/photos/958545/pexels-photo-958545.jpeg'

with app.app_context():

    # Delete All Rows To Work On A Clean Slate
    User.query.delete()
    Food.query.delete()
    Order.query.delete()

    # Populate User table
    for x in range(10):
        user = User(username=fake.name(), password_hash=fake.word())
        db.session.add(user)
        db.session.commit()
    print('Populated User table')

    # Populate Food table
    for x in range(25):
        ingredients = []
        for i in range(5):
            ingredients.append(fake.ingredient())
        food = Food(name=fake.dish(), description=fake.dish_description(), category=fake.ethnic_category(), price=fake.random_number(digits=3), image=img)
        db.session.add(food)
        db.session.commit()
    print('Populated Food table')
    
    # Populate restaurantspizzas table
    for x in range (100):
        order = Order(quantity=fake.random_digit_not_null(), user_id=fake.random_int(min=1, max=10), food_id=fake.random_int(min=1, max=25))
        db.session.add(order)
        db.session.commit()
    print('Populated Orders table')