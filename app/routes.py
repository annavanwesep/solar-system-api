
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
            "name": planet.planet_name,
            "description": planet.description, 
            "potential for life": planet.potential_for_life,
            "number_of_moons": planet.number_of_moons})
    
    return jsonify(planets_dict)

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.planet_name,
        "description": planet.description,
        "potential for life": planet.potential_for_life,
        "number_of_moons": planet.number_of_moons
        }

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
    planet = Planet.query.get(planet_id)

    # for planet in solar_system_planets:
    #     if planet.id == planet_id:
    #         return planet
    return planet if planet else abort(make_response({"message":f"planet {planet_id} not found"}, 404))

@planets_bp.route("/<animal_id>", methods=['PUT'])
def update_one_planet(planet_id):
    #Get the data from the request body
    request_body = request.get_json()
    
    planet_to_update = validate_planet(planet_id)
    
    db.session.commit()
    
    return planet_to_update(), 200

@planets_bp.route("/<planet_id>", methods=['DELETE'])
def delete_one_planet(planet_id):
    
    planet_to_delete = validate_planet(planet_id)
    
    db.session.delete(planet_to_delete)
    db.session.commit()
    
    return f"Planet {planet_to_delete.name} is deleted!", 200


# # Refactor : 
# solar_system_planets = [
#     Planet(1, "Mercury", "smallest planet", "not conducive", 0), 
#     Planet(2, "Venus", "hottest planet", "could accommodate Earthly life, such as 'extremophile' microbes", 0), 
#     Planet(3, "Earth", "home planet", "life abundant", 1), 
#     Planet(4, "Mars", "dusty, cold desert", "scientists don't expect to find living things thriving", 2), 
#     Planet(5, "Jupiter", "more than twice as massive than the other planets combined", "not conducive", 80), 
#     Planet(6, "Saturn", "adorned with a dazzling, complex system of icy rings", "not conducive", 82), 
#     Planet(7, "Uranus", "unique tilt makes it appear to spin on its side", "not conducive", 27), 
#     Planet(8, "Neptune", "most distant", "not conducive", 14)
# ]

# Creating a Planet Endpoint
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['POST'])

def create_planets():    # check if columns in response body? If not return 400 "Invalid Request"?
    request_body = request.get_json()
    print(request_body)
    new_planet = Planet(planet_name=request_body["name"], 
                        description=request_body["description"],
                        potential_for_life=request_body["potential_for_life"],
                        number_of_moons=request_body["number_of_moons"])    

    db.session.add(new_planet) 
    db.session.commit()    
    
    return {"id":new_planet.id,
            "name":new_planet.planet_name,
            "msg": "Successfully created"}, 201


