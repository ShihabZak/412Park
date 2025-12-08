from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import sqlite3
import json

app = Flask(__name__)
CORS(app)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route('/api/spots/<hall>')
def get_spots(hall):
    spots = [
        {"number": i, "occupied": False, "hall": hall}
        for i in range(1, 11)
    ]
    return jsonify({"hall": hall, "spots": spots})

@app.route('/api/spots/<hall>/<int:spot>', methods=['POST'])
def update_spot(hall, spot):
    return jsonify({
        "success": True,
        "message": f"Spot {spot} in {hall} updated",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/overview')
def overview():
    halls = ['alumni', 'information', 'towers', 'petersen', 
             'lawrence', 'frickfinearts', 'cathedral', 'recreation']
    
    overview_data = []
    for hall in halls:
        overview_data.append({
            "id": hall,
            "name": hall.replace('_', ' ').title(),
            "total_spots": 10,
            "available_spots": 5,  
            "availability": "50%"
        })
    
    return jsonify({"halls": overview_data})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
