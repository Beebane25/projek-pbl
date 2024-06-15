from flask import Flask, request, jsonify
import mysql.connector
import json

app = Flask(__name__)

# Konfigurasi database
db_config = {
    'database': 'webhook_db'
}

def save_payload_to_db(payload):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        add_payload = ("INSERT INTO webhook_payloads (payload) VALUES (%s)")
        cursor.execute(add_payload, (json.dumps(payload),))
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        save_payload_to_db(payload)
        return jsonify({'status': 'success', 'message': 'Payload received and stored'}), 200
    return jsonify({'status': 'error', 'message': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(debug=True)
