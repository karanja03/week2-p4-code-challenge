# from server.config.models import Heroes, Powers, Heroes_Powers
# from server.config.app import db

# # Create heroes
# heroes1 = Heroes(name="John Black", super_name="SuperMan")
# heroes2 = Heroes(name="Rock Bottom", super_name="BatMan")
# heroes3 = Heroes(name="Jason Starthman", super_name="IronMan")
# heroes4 = Heroes(name="Jack Daniels", super_name="Hulk")
# heroes5 = Heroes(name="Johny Walker", super_name="")

# # Create powers
# powers1 = Powers(name="Super Strength", description="Incredible physical power, unmatched strength")
# powers2 = Powers(name="Flight", description="Soaring through skies, defying gravity")
# powers3 = Powers(name="Telekinesis", description="Objects moved with focused thought.")
# powers4 = Powers(name="Invisibility", description="Unseen, hidden from plain sight.")
# powers5 = Powers(name="Time Manipulation", description="Control past, present, future events.")

# # Create Heroes_Powers associations with strengths
# hp1 = Heroes_Powers(strength='Strong', hero=heroes3, power=powers4)
# hp2 = Heroes_Powers(strength='Weak', hero=heroes2, power=powers5)
# hp3 = Heroes_Powers(strength='Average', hero=heroes1, power=powers3)
# hp4 = Heroes_Powers(strength='Strong', hero=heroes4, power=powers2)
# hp5 = Heroes_Powers(strength='Average', hero=heroes5, power=powers1)

# # Add objects to the session and commit to the database
# db.session.add_all([heroes1, heroes2, heroes3, heroes4, heroes5, powers1, powers2, powers3, powers4, powers5, hp1, hp2, hp3, hp4, hp5])
# db.session.commit()

# print("Data seeded successfully.")



from config.models import Heroes, Powers, Heroes_Powers
from config.app import db, app
import random


with app. app_context():

# Define the data for powers and heroes
    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]

    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"}
    ]

    # Create heroes
    for hero_data in heroes_data:
        hero = Heroes(**hero_data)
        db.session.add(hero)

    # Create powers
    for power_data in powers_data:
        power = Powers(**power_data)
        db.session.add(power)

    # Commit the changes to the database to generate IDs
    db.session.commit()

    # Define strength levels
    strengths = ["Strong", "Weak", "Average"]

    # Add powers to heroes
    heroes = Heroes.query.all()
    for hero in heroes:
        num_powers = random.randint(1, 3)
        for _ in range(num_powers):
            power = random.choice(Powers.query.all())
            strength = random.choice(strengths)
            hero_power = Heroes_Powers(hero_id=hero.id, power_id=power.id, strength=strength)
            db.session.add(hero_power)

    # Commit the changes to the database
    db.session.commit()

    print("Data seeded successfully.")
