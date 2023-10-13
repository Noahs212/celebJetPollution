from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual AviationStack API key
API_KEY = "947ef17ad2420b1a1d3d34058504eac3"

@app.route('/')
def index():
    return 'Welcome to the AviationStack API!'
# Define a route to retrieve flight information
@app.route('/getflight', methods=['GET'])
def get_historical_flight_info():
    # Define the base URL
    base_url = 'http://api.aviationstack.com/v1/flights?access_key=947ef17ad2420b1a1d3d34058504eac3'

    # Make the GET request
    response = requests.get(base_url)
   
    print(response)
    print(response.status_code)
    if response.status_code == 200:
        flight_data = response.json()
        return jsonify(flight_data)
    else:
        return jsonify({'error': 'Failed to retrieve historical flight information'}), 500

if __name__ == '__main__':
    app.run(debug=True)
