from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# Sample data
planets = []

@app.route('/planets', methods=['GET'])
def get_planets():
    return jsonify(planets)

@app.route('/planets', methods=['POST'])
def add_planet():
    data = request.get_json()
    planet = {
        'ID': str(uuid.uuid4()),
        'Nom': data.get('Nom'),
        'Découvreur': data.get('Découvreur'),
        'Date de Découverte': data.get('Date de Découverte'),
        'Masse': data.get('Masse'),
        'Rayon': data.get('Rayon'),
        'Distance': data.get('Distance'),
        'Type': data.get('Type'),
        'Statut': data.get('Statut'),
        'Atmosphère': data.get('Atmosphère'),
        'Température Moyenne': data.get('Température Moyenne'),
        'Période Orbitale': data.get('Période Orbitale'),
        'Nombre de Satellites': data.get('Nombre de Satellites'),
        'Présence d’Eau': data.get('Présence d’Eau')
    }
    planets.append(planet)
    return jsonify(planet), 201

@app.route('/planets/<planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = next((p for p in planets if p['ID'] == planet_id), None)
    if planet is None:
        return jsonify({'error': 'Planet not found'}), 404
    return jsonify(planet)

@app.route('/planets/<planet_id>', methods=['PUT'])
def update_planet(planet_id):
    data = request.get_json()
    planet = next((p for p in planets if p['ID'] == planet_id), None)
    if planet is None:
        return jsonify({'error': 'Planet not found'}), 404

    planet.update({
        'Nom': data.get('Nom', planet['Nom']),
        'Découvreur': data.get('Découvreur', planet['Découvreur']),
        'Date de Découverte': data.get('Date de Découverte', planet['Date de Découverte']),
        'Masse': data.get('Masse', planet['Masse']),
        'Rayon': data.get('Rayon', planet['Rayon']),
        'Distance': data.get('Distance', planet['Distance']),
        'Type': data.get('Type', planet['Type']),
        'Statut': data.get('Statut', planet['Statut']),
        'Atmosphère': data.get('Atmosphère', planet['Atmosphère']),
        'Température Moyenne': data.get('Température Moyenne', planet['Température Moyenne']),
        'Période Orbitale': data.get('Période Orbitale', planet['Période Orbitale']),
        'Nombre de Satellites': data.get('Nombre de Satellites', planet['Nombre de Satellites']),
        'Présence d’Eau': data.get('Présence d’Eau', planet['Présence d’Eau'])
    })
    return jsonify(planet)

@app.route('/planets/<planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    global planets
    planets = [p for p in planets if p['ID'] != planet_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)