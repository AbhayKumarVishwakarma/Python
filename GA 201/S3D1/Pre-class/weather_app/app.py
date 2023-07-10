from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}


@app.route('/weather', methods=['GET'])
def get_all_weather():
    if len(weather_data) == 0:
        return jsonify({'message': 'Not found any city in data'}), 404

    return jsonify(weather_data)


@app.route('/weather/<string:city>', methods=['GET'])
def get_weather(city):
    if city in weather_data:
        return jsonify(weather_data[city])
    else:
        return jsonify({'error': 'City not found'}), 404


@app.route('/weather', methods=['POST'])
def add_weather():
    data = request.get_json()

    if 'city' not in data or 'temperature' not in data or 'weather' not in data:
        return jsonify({'message': "Error, Invalid data!"}), 400

    city = data['city']
    temperature = data['temperature']
    weather = data['weather']

    weather_data[city] = {'temperature': temperature, 'weather': weather}

    return jsonify({'message': f'Weather data for {city} added successfully', 'data': data})


@app.route('/weather/<string:city>', methods=['PUT'])
def update_weather(city):
    data = request.get_json()

    if city not in weather_data:
        return jsonify({'message': f'{city} not found!'}), 404

    city_data = weather_data[city]

    if 'temperature' in data:
        city_data['temperature'] = data['temperature']
    if 'weather' in data:
        city_data['weather'] = data['weather']

    return jsonify({'message': f'Weather data for {city} updated successfully',
                    'data': {'city': city, 'temperature': city_data['temperature'], 'weather': city_data['weather']}})


@app.route('/weather/<string:city>', methods=['DELETE'])
def delete_weather(city):
    if city not in weather_data:
        return jsonify({'message': f'{city} not found!'}), 404

    del weather_data[city]
    return jsonify({'message': f'Weather data for {city} deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)

