


from config.models import Heroes, Powers, Heroes_Powers
from server.app import db, app
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
