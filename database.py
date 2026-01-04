import sqlite3
from datetime import datetime

def init_database():
    conn = sqlite3.connect('parking.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS parking_spots
                 (hall_id TEXT, spot_number INTEGER, is_occupied BOOLEAN,
                  updated_at TIMESTAMP,
                  UNIQUE(hall_id, spot_number))''')
    
    halls = ['alumni', 'information', 'towers', 'petersen', 
             'lawrence', 'frickfinearts', 'cathedral', 'recreation']
    
    for hall in halls:
        for spot in range(1, 11):
            c.execute('''INSERT OR IGNORE INTO parking_spots 
                         (hall_id, spot_number, is_occupied, updated_at)
                         VALUES (?, ?, ?, ?)''',
                     (hall, spot, False, datetime.now()))
    
    conn.commit()
    
    c.execute('SELECT COUNT(*) FROM parking_spots')
    count = c.fetchone()[0]
    print(f"Database initialized with {count} parking spots")
    
    conn.close()

if __name__ == '__main__':
    init_database()
