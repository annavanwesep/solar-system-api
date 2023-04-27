from app import db

# Class 'Planet' because SQL likes singular class names
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    planet_name = db.Column(db.String)
    description = db.Column(db.String)
    potential_for_life = db.Column(db.String)
    number_of_moons = db.Column(db.Integer)


    def get_planet_info(self):
        return f"{self.id} | Planet Name: {self.planet_name}  Description: {self.description} Potential for Life: {self.potential_for_life}  Number of Moons: {self.number_of_moons}"