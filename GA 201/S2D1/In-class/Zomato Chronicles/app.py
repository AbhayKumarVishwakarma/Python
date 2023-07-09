from flask import Flask, jsonify, request
app = Flask(__name__)

menu = [
    {
        'id': 1,
        'name': 'Pizza',
        'price': 399,
        'availability': "yes",
        'pieces': 10
    },
    {
        'id': 2,
        'name': 'Burger',
        'price': 199,
        'availability': "yes",
        'pieces': 15
    }
]

order = [
    {
        "customerName": "Ankit",
        "dishId": 1,
        "orderId": 1,
        "status": "delivered"
    }
]


@app.route('/')
def home():
    return "Welcome to Zesty Zomato!"


@app.route('/menu', methods=['GET'])
def get_menu():
    global menu
    return jsonify(menu)


@app.route('/menu', methods=['POST'])
def add_dish():
    global menu
    data = request.get_json()
    new_dish = {
        'id': data.get('id'),
        'name': data.get('name'),
        'price': data.get('price'),
        'availability': data.get('availability'),
        'pieces': data.get('pieces')
    }
    menu.append(new_dish)
    return jsonify({'message': 'New dish added successfully'})


@app.route('/menu/<int:dish_id>', methods=['DELETE'])
def remove_dish(dish_id):
    global menu
    for dish in menu:
        if dish['id'] == dish_id:
            menu.remove(dish)
            return jsonify({'message': 'Dish removed successfully'})
    return jsonify({'message': 'Invalid dish ID'})


@app.route('/menu/<int:dish_id>', methods=['PUT'])
def update_dish_availability(dish_id):
    global menu
    data = request.get_json()
    new_availability = data.get('availability')
    for dish in menu:
        if dish['id'] == dish_id:
            dish['availability'] = new_availability
            if new_availability == "no":
                dish['pieces'] = 0
            else:
                pieces = data.get('pieces')
                dish['pieces'] = pieces
            return jsonify({'message': 'Dish availability updated successfully'})
    
    return jsonify({'message': 'Invalid dish ID'})



@app.route('/orders', methods=['POST'])
def place_order():
    global order, menu

    data = request.get_json()
    dishId = data.get('dishId')

    for dish in menu:
        if dish['id'] == dishId:
            if dish['availability'] == "yes":
                order.append(data)
                return jsonify({'message': 'Order placed successfully'})
            return jsonify({'message': 'Sorry, dish is not available!'})

    return jsonify({'message': 'Invalid order. Please check the dish IDs and availability.'})


@app.route('/orders/<int:orderId>', methods=['PUT'])
def updateOrder(orderId):
    global order

    data = request.get_json()
    newStatus = data.get('status')

    for o in order:
        if o['orderId'] == orderId:
            o['status'] = newStatus
            return jsonify({'message': 'Order status updated successfully'})

    return jsonify({'message': 'Invalid order ID'})


@app.route('/orders', methods=['GET'])
def get_order():
    return jsonify(order)



if __name__ == '__main__':
    app.run(debug=True)
