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
    
# Define a Resource for the "/restaurants" route
class GetHeroes(Resource):
    def get(self):
        # Retrieve all restaurants from the database
        heroes = Heroes.query.all()
        # Serialize the restaurants using the schema
        response = make_response(heroes_schema .dump(heroes), 200)

        return response

class RestaurantByID(Resource):
    def get(self, id):
        # Retrieve a single restaurant by its ID
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            # Serialize the restaurant using the schema for a single object
            response = make_response(restaurant_schema.dump(restaurant), 200)
        else:
            # If the restaurant with the specified ID doesn't exist, return a 404 response
            response_dict = {"error": "Restaurant not found"}
            response = make_response(response_dict, 404)

        return response





