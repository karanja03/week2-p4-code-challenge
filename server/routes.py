from flask import  make_response, request, jsonify
from flask_restful import  Resource
from server import db ,api
from server.schema import hero_schema, heroes_schema, power_schema, powers_schema, heroespower_schema, heroespowers_schema
from server.models import Heroes, Heroes_Powers, Powers

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
        




