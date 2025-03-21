import os
import requests
import json
import redis
from flask import Flask, jsonify, request

# Configuration
REDIS_HOST = os.getenv('REDIS_HOST', 'redis-12047.c334.asia-southeast2-1.gce.redns.redis-cloud.com')
REDIS_PORT = int(os.getenv('REDIS_PORT', 12047))
REDIS_DB = int(os.getenv('REDIS_DB', 0))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', 'ZN4J5MXIu3TNchvB7VpY9tMR1VosNQue')  # Add this line if your Redis instance requires a password
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', '3VJJUHR2YD5NMBZ4MGTQ2B5GP')
WEATHER_API_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

# Initialize Redis
cache = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD)

# Initialize Flask
app = Flask(__name__)

def get_weather(location):
    url = f"{WEATHER_API_URL}{location}?unitGroup=us&key={WEATHER_API_KEY}&contentType=json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e.response.status_code} {e.response.text}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

@app.route('/weather/<location>', methods=['GET'])
def weather(location):
    cached_data = cache.get(location)
    if cached_data:
        return jsonify({"source": "cache", "data": json.loads(cached_data.decode('utf-8'))})

    weather_data = get_weather(location)
    if weather_data:
        cache.set(location, json.dumps(weather_data), ex=43200)  # Cache for 12 hours
        return jsonify({"source": "api", "data": weather_data})
    else:
        return jsonify({"error": "Unable to fetch weather data"}), 500

if __name__ == '__main__':
    app.run(debug=True)