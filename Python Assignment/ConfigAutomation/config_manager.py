import yaml
import json
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

# Function to read the configuration file
def read_config(file_path):
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
            return config
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except yaml.YAMLError as exc:
        print(f"Error reading YAML file: {exc}")
        return None

# Function to save the dictionary as JSON data in the database
def save_to_database(data, db_path='config.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS config (id INTEGER PRIMARY KEY, json_data TEXT)')
    json_data = json.dumps(data)
    cursor.execute('INSERT INTO config (json_data) VALUES (?)', (json_data,))
    conn.commit()
    conn.close()

# Function to fetch the data from the database
def fetch_from_database(db_path='config.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT json_data FROM config ORDER BY id DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()
    if row:
        return json.loads(row[0])
    return {}

# Flask route to fetch the configuration data
@app.route('/config', methods=['GET'])
def get_config():
    data = fetch_from_database()
    return jsonify(data)

def main():
    config_file_path = 'config.yaml'
    config_data = read_config(config_file_path)
    
    if config_data:
        extracted_data = {
            'database': config_data.get('database', {}),
            'server': config_data.get('server', {})
        }
        
        save_to_database(extracted_data)
        print("Configuration data saved to the database.")

if __name__ == '__main__':
    main()
    app.run(debug=True)
