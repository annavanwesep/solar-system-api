from flask import Blueprint, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['GET'])
def handle_planets():
    planets_dict = []
    for planet in solar_system_planets:
        planets_dict.append(
            {"id": planet.id,
             "name": planet.name,
             "description": planet.description, 
             "potential for life": planet.potential_for_life})
    return jsonify(planets_dict)

class Planet():
    def __init__(self, id, name, description, potential_for_life):
        self.id = id
        self.name = name
        self.description = description
        self.potential_for_life = potential_for_life

solar_system_planets = [
    Planet(1, "Mercury", "smallest planet", "not conducive"), 
    Planet(2, "Venus", "hottest planet", "could accommodate Earthly life, such as 'extremophile' microbes"), 
    Planet(3, "Earth", "home planet", "life abundant"), 
    Planet(4, "Mars", "dusty, cold desert", "scientists don't expect to find living things thriving"), 
    Planet(5, "Jupiter", "more than twice as massive than the other planets combined", "not conducive"), 
    Planet(6, "Saturn", "adorned with a dazzling, complex system of icy rings", "not conducive"), 
    Planet(7, "Uranus", "unique tilt makes it appear to spin on its side", "not conducive"), 
    Planet(8, "Neptune", "most distant", "not conducive")
]