from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('parking.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/health')
def health():
    return jsonify({
        'status': 'ok',
        'message': 'Flask server is running!'
    })

@app.route('/spots', methods=['GET'])
def get_spots():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM parking_spots')
    rows = cursor.fetchall()
    conn.close()
    
    # Organize spots by their original sections
    top_ids = ['petersen', 'recreation', 'information']
    middle_ids = ['alumni', 'towers', 'cathedral']
    bottom_ids = ['sennott', 'lawrence', 'frickfinearts']
    
    locations = {'top': [], 'middle': [], 'bottom': []}
    
    for row in rows:
        spot = {
            'id': row['id'],
            'name': row['name'],
            'spots': row['available_spots'],  # Changed from 'spots' to 'available_spots'
            'total': row['total_spots'],
            'price': row['price']
        }
        
        if row['id'] in top_ids:
            locations['top'].append(spot)
        elif row['id'] in middle_ids:
            locations['middle'].append(spot)
        elif row['id'] in bottom_ids:
            locations['bottom'].append(spot)
    
    return jsonify(locations)

@app.route('/spots/<spot_id>', methods=['PUT'])
def update_spot(spot_id):
    data = request.json
    new_available = data.get('spots')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE parking_spots SET available_spots = ? WHERE id = ?', (new_available, spot_id))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'message': 'Spot updated'})

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, port=5000)