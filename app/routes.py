
from app import db
from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['GET'])
def handle_planets():
    planets_dict = []
    solar_system_planets = Planet.query.all()
    for planet in solar_system_planets:
        planets_dict.append(
            {"id": planet.id,
            "name": planet.name,
            "description": planet.description, 
            "potential for life": planet.potential_for_life,
            "number_of_moons": planet.number_of_moons})
    
    return jsonify(planets_dict)

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "potential for life": planet.potential_for_life,
        "number_of_moons": planet.number_of_moons
        }

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in solar_system_planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"planet {planet_id} not found"}, 404))

class Planet():
    def __init__(self, id, name, description, potential_for_life, number_of_moons):
        self.id = id
        self.name = name
        self.description = description
        self.potential_for_life = potential_for_life
        self.number_of_moons = number_of_moons

# Refactor : 
solar_system_planets = [
    Planet(1, "Mercury", "smallest planet", "not conducive", 0), 
    Planet(2, "Venus", "hottest planet", "could accommodate Earthly life, such as 'extremophile' microbes", 0), 
    Planet(3, "Earth", "home planet", "life abundant", 1), 
    Planet(4, "Mars", "dusty, cold desert", "scientists don't expect to find living things thriving", 2), 
    Planet(5, "Jupiter", "more than twice as massive than the other planets combined", "not conducive", 80), 
    Planet(6, "Saturn", "adorned with a dazzling, complex system of icy rings", "not conducive", 82), 
    Planet(7, "Uranus", "unique tilt makes it appear to spin on its side", "not conducive", 27), 
    Planet(8, "Neptune", "most distant", "not conducive", 14)
]

# Creating a Planet Endpoint
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['POST'])

def create_planets():
        
    # check if columns in response body? If not return 400 "Invalid Request"?
    request_body = request.get_json()
    new_planet = Planet(id = request_body["id"],
                        planet_name = request_body["name"], 
                        description = request_body["description"],
                        potential_for_life = request_body["potential_for_life"],
                        number_of_moons = request_body["number_of_moons"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"{new_planet.id} | Planet Name: {new_planet.name}  Description: {new_planet.description} Potential for Life: {new_planet.potential_for_life}  Number of Moons: {new_planet.number_of_moons} created successfully! 201")

from app import db

# Class 'Planet' because SQL likes singular class names
# class Planet(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     planet_name = db.Column(db.String)
#     description = db.Column(db.String)
#     potential_for_life = db.Column(db.String)
#     number_of_moons = db.Column(db.Integer)
