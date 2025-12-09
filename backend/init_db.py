import sqlite3
import sys

try:
    print("Starting database creation...")
    
    # Create database and table
    conn = sqlite3.connect('parking.db')
    print("Connected to database")
    
    cursor = conn.cursor()
    
    # Create parking spots table
    print("Creating table...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS parking_spots (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        spots INTEGER NOT NULL,
        price TEXT NOT NULL
    )
    ''')
    print("Table created")
    
    # Insert the parking locations
    print("Inserting data...")
    locations = [
        ('petersen', 'Petersen Event Center', 10, '$2.50/hour'),
        ('recreation', 'Pitt Recreation Center', 10, '$2.00/hour'),
        ('information', 'IS Building', 10, '$3.00/hour'),
        ('alumni', 'Alumni Hall', 10, '$2.75/hour'),
        ('towers', 'Litchfield Towers', 10, '$2.00/hour'),
        ('cathedral', 'Cathedral of Learning', 10, '$3.50/hour'),
        ('sennott', 'Sennott Square', 10, '$2.25/hour'),
        ('lawrence', 'Lawrence Hall', 10, '$2.00/hour'),
        ('frickfinearts', 'Frick Fine Arts', 10, '$2.50/hour')
    ]
    
    cursor.executemany('INSERT OR REPLACE INTO parking_spots VALUES (?, ?, ?, ?)', locations)
    print("Data inserted")
    
    conn.commit()
    print("Changes committed")
    
    conn.close()
    print("Database created successfully!")
    
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr)
    sys.exit(1)