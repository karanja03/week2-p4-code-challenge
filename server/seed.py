
from models import   Heroes, Heroes_Powers,Powers
from models import db
from app import app


with app.app_context():
    # Create heroes
    heroes1 = Heroes(name="John Black ", super_name="SuperMan")
    heroes2 = Heroes(name="Rock Bottom", super_name="BatMan")
    heroes3 = Heroes(name="Jason Starthman", super_name="IronMan")
    heroes4 = Heroes(name ="Jack Daniels", super_name = "Hulk")
    heroes5 = Heroes(name ="Johny Walker", super_name = "")

    # Create Power
    powers1 = Powers(name="Super Strength", description="Incredible physical power, unmatched strength")
    powers2 = Powers(name="Flight", description = "Soaring through skies, defying gravity")
    powers3 = Powers(name="Telekinesis", description="Objects moved with focused thought.")
    powers4 = Powers(name="Invisibility", description="Unseen, hidden from plain sight.")
    powers5 = Powers(name = "Time Manipulation", description = "Control past, present, future events.")


    # Create restaurant_pizzas associations with prices
    rp1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=12)
    rp2 = RestaurantPizza(restaurant=restaurant1, pizza=pizza2, price=14)
    rp3 = RestaurantPizza(restaurant=restaurant2, pizza=pizza2, price=13)
    rp4 = RestaurantPizza(restaurant=restaurant2, pizza=pizza3, price=15)
    rp5 = RestaurantPizza(restaurant=restaurant3, pizza=pizza1, price=11)

# Add objects to the session and commit to the database
    db.session.add_all([restaurant1, restaurant2, restaurant3, pizza1, pizza2, pizza3, rp1, rp2, rp3, rp4, rp5])
    db.session.commit()

print("Data seeded successfully.")