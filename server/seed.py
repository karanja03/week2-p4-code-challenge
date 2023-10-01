
from config.models import   Heroes, Heroes_Powers,Powers
from config.models import db
from config.app import app


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
    powers5 = Powers(name="Time Manipulation", description = "Control past, present, future events.")


    # Create Heroes_Powersassociations with prices
    hp1 = Heroes_Powers(strength='Strong',  hero_id=heroes3, power_id=powers4)
    hp2 = Heroes_Powers(strength='Weak' , hero_id=heroes2, power_id=powers5)
    hp3 = Heroes_Powers(strength='Average',  hero_id=heroes1, power_id=powers3)
    hp4 = Heroes_Powers(strength='Strong',  hero_id=heroes4, power_id=powers2)
    hp5 = Heroes_Powers(strength='Average',  hero_id=heroes5, power_id=powers1)

# Add objects to the session and commit to the database
    db.session.add_all([heroes1, heroes2, heroes3, heroes4, heroes5, powers1, powers2, powers3, powers4, powers5, hp1,  hp2, hp3 , hp4, hp5])
    db.session.commit()

print("Data seeded successfully.")