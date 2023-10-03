from flask import  make_response, request, jsonify
from flask_restful import  Resource
from server import db ,api
from schema import hero_schema, heroes_schema, power_schema, powers_schema, heroespower_schema, heroespowers_schema
from server.config.models import Heroes, Heroes_Powers, Powers

# Define a Resource for the home route ("/")
class Home(Resource):
    def get(self):
        # Create a response dictionary
        response_dict = {"home": "Welcome to my Heroes Api.I hope you have an amaing experience using it"}

        # Create an HTTP response with the dictionary and status code 200 (OK)
        response = make_response(response_dict, 200)

        return response
    
# Define a Resource for the "/heroes" route
class GetHeroes(Resource):
    def get(self):
        # Retrieve all restaurants from the database
        heroes = Heroes.query.all()
        # Serialize the restaurants using the schema
        response = make_response(heroes_schema .dump(heroes), 200)

        return response
    
    # Define a Resource for the "/heroes/id" route


class GetHeroesByID(Resource):
    def get(self, id):
        # Retrieve a single hero by its ID
        hero =Heroes.query.filter_by(id=id).first()
        if hero:
            # Serialize the hero using the schema for a single object
            response = make_response(hero_schema.dump(hero), 200)
        else:
            # If the hero with the specified ID doesn't exist, return a 404 response
            response_dict = {"error": "Restaurant not found"}
            response = make_response(response_dict, 404)

        return response

# Define a Resource for the "/powers" route

class GetPowers(Resource):
    def get(self):
        # Retrieve a single restaurant by its ID
        powers =Powers.query.all()
        response = make_response(powers_schema .dump(powers), 200)

        return response
    
    # Define a Resource for the "/powers/id" route

    
class GetPowersByID(Resource):
    def get(self, id):
        # Retrieve a single power by its ID
        power =Powers.query.filter_by(id=id).first()
        if power:
            # Serialize the hero using the schema for a single object
            response = make_response(power_schema.dump(power), 200)
        else:
            # If the hero with the specified ID doesn't exist, return a 404 response
            response_dict = {"error": "Restaurant not found"}
            response = make_response(response_dict, 404)

        return response
    
# Update an existing Power

    def patch(self, id):
        try:
            # Retrieve the existing Power by its ID
            power = Powers.query.get(id)

            if not power:
                response_dict = {"error": "Power not found"}
                return make_response(response_dict, 404)

            # Get the updated description from the request JSON data
            updated_description = request.json.get('description')

            if updated_description is None:
                response_dict = {"error": "Description is required"}
                return make_response(response_dict, 400)

            # Update the Power's description
            power.description = updated_description

            # Commit the changes to the database
            db.session.commit()

            # Serialize the updated Power using the schema
            response = make_response(power_schema.dump(power), 200)

        except Exception as e:
            response_dict = {"error": str(e)}
            response = make_response(response_dict, 500)

        return response    
    
    
    # Post route for hero_powers route    
    
    
class PostHeroPowers(Resource):
        
    def post(self):
        try:
            # Extract data from the JSON request
            data = request.json

            # Create a new HeroPower object
            new_hero_power =Heroes_Powers(
                hero_id=data['hero_id'],
                power_id=data['power_id'],
                strength=data['strength']
            )

            # Add the new HeroPower to the database
            db.session.add(new_hero_power)
            db.session.commit()

            # Serialize the created HeroPower using the schema
            response = make_response(heroespower_schema.dump(new_hero_power), 201)

        except Exception as e:
                response_dict = {"error": str(e)}
                response = make_response(response_dict, 500)

        return response
        
api.add_resource(Home, "/")
# Add the Heroes resource to handle the "/heroes" route
api.add_resource(GetHeroes, "/heroes")

# Add the PostHeroPowers resource to handle the route '/heropowers'
api.add_resource(PostHeroPowers, "/hero_powers")
# Add the GetPowersByID resource to handle the "/powers/<int:id>" route
api.add_resource(GetPowersByID, "/powers/<int:id>")
# Add the GetHeroesByID resource to handle the "/heroes/<int:id>" route
api.add_resource(GetHeroesByID, "/heroes/<int:id>")
# Add the  Powers resource to handle the "/ powers" route
api.add_resource( GetPowers, "/powers")
                
        
        
        




