from flask import Flask, jsonify

app = Flask(__name__)

# In-memory data store for example purposes
sensor_data = {
    "temperature": 22.5
}

@app.route('/temperature', methods=['GET'])
def get_temperature():
    return jsonify(sensor_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
