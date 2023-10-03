from flask import  make_response, request, jsonify
from flask_restful import  Resource
from config.models import db 
from config import api
# from schema import hero_schema, heroes_schema, power_schema, powers_schema, heroespower_schema, heroespowers_schema
from config.models import Heroes, Heroes_Powers, Powers

    
# Define a Resource for the "/heroes" route
class GetHeroes(Resource):
    def get(self):
        # Retrieve all heroesfrom the database
        
        try:
            heroes = Heroes.query.all()
            # Serialize the restaurants using the schema
            heroes_list = [hero.to_dict() for hero in heroes]
            response = make_response(jsonify(heroes_list), 200)
            return response
        except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500)
    
    # Define a Resource for the "/heroes/id" route


class GetHeroesByID(Resource):
    def get(self, id):
        # Retrieve a single hero by its ID
        try:
            hero =Heroes.query.filter_by(id=id).first()
            if hero:
                # Serialize the hero using the schema for a single object
                response = make_response(hero.to_dict(), 200)
            else:
                # If the hero with the specified ID doesn't exist, return a 404 response
                response_dict = {"error": "Hero not found"}
                response = make_response(response_dict, 404)

            return response
        
        except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500)

# Define a Resource for the "/powers" route

class GetPowers(Resource):
    def get(self):
        # Retrieve a single restaurant by its ID
        try:
            powers =Powers.query.all()
            powers_list = [power.to_dict() for power in powers]
            response = make_response(jsonify(powers_list), 200)
            return response
        
        except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500)
    
    # Define a Resource for the "/powers/id" route

    
class PowersByID(Resource):
    def get(self, id):
        
        try:
            power = Powers.query.filter_by(id = id).first()

            if power:
                response = make_response(power.to_dict(), 200)
            
            else:
                response_dict = {"error": "Power not found"}
                response = make_response(response_dict, 404)

            return response
        
        except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500) 
           
# Update an existing Power

    def patch(self, id):
        try:
            # Retrieve the existing Power by its ID
            power = Powers.query.get(id)

            if not power:
                response_dict = {"error": "Power not found"}
                return make_response(response_dict, 404)
            data = request.get_json()
            if "name" in data:
                    power.name = data["name"]

            if "description" in data:
                    power.description = data["description"]

            db.session.commit()

            response = make_response(power.to_dict(), 200)
            return response
               
        except Exception as e:
                error_message = str(e)
                return make_response(jsonify({"error": error_message}), 500)

    
    # Post route for hero_powers route    
    
    
class PostHeroPowers(Resource):
        
    def post(self):
        try:
            # Extract data from the JSON request
            data = request.get_json()

            # Create a new HeroPower object
            hero_id=data.get['hero_id'],
            power_id=data.get['power_id'],
            strength=data.get['strength']
            
            if not strength or not power_id or not hero_id:
                return {"errors": ["validation errors"]}, 400
            
            power = Powers.query.get(power_id)
            hero = Heroes.query.get(hero_id)

            if not power or not hero:
                return {"errors": ["Power or Hero not found"]}, 404
            
            hero_power = Heroes_Powers(strength = strength, power_id = power_id, hero_id = hero_id)

            db.session.add(hero_power)
            db.session.commit()

            # Add the new HeroPower to the database
            db.session.add(hero_power)
            db.session.commit()

            hero_data = {
                "id": hero.id,
                "name": hero.name,
                "powers":[
                    {
                        "id": power.id,
                        "name": power.name,
                        "description": power.description,
                    }
                ],
            }

            return hero_data, 201
        
        except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500)
            
api.add_resource(GetHeroes, "/heroes")
api.add_resource(PostHeroPowers, "/hero_powers")
api.add_resource(PowersByID, "/powers/<int:id>")
api.add_resource(GetHeroesByID, "/heroes/<int:id>")
api.add_resource( GetPowers, "/powers")
                
        
        
        




