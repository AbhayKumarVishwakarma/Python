from flask import Flask, render_template, request, redirect
# from flask_socketio import SocketIO

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your-secret-key'
# socketio = SocketIO(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zomato.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)


# class Dish(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     available = db.Column(db.String)
#
#
#
# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     customer_name = db.Column(db.String(100), nullable=False)
#     dish_id = db.Column(db.Integer)
#     status = db.Column(db.String(20), nullable=False, default='received')


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
def index():
    return 'Welcome to Zomato Chronicles: The Great Food Fiasco!'


# WebSocket endpoint for handling real-time updates
# @socketio.on('connect')
# def handle_connect():
#     print('Client connected')
#     # Send initial order status to the connected client
#     socketio.emit('initial_orders', order, broadcast=False)


@app.route('/dishes/create', methods=['GET', 'POST'])
def create_dish():
    global menu
    if request.method == 'POST':
        new_dish = {
            'id': request.form['id'],
            'name': request.form['name'],
            'price': request.form['price'],
            'availability': request.form['available']
        }
        menu.append(new_dish)
        return redirect('/dishes')
    else:
        return render_template('add_dish.html')


@app.route('/dishes', methods=['GET'])
def list_dishes():
    global menu
    print(menu)
    return render_template('dishes.html', dishes=menu)


@app.route('/dishes/update/<int:dish_id>', methods=['GET', 'POST'])
def update_dish(dish_id):
    global menu
    if request.method == 'POST':
        for dish in menu:
            if int(dish['id']) == int(dish_id):
                dish['availability'] = request.form['available']
                return redirect('/dishes')
    else:
        for dish in menu:
            if int(dish['id']) == int(dish_id):
                return render_template('update_dish.html', dish=dish)


@app.route('/dishes/delete/<int:dish_id>')
def delete_dish(dish_id):
    global menu
    for dish in menu:
        if int(dish['id']) == int(dish_id):
            menu.remove(dish)
            print("delete")
            return redirect('/dishes')
        else:
            return render_template('error.html', error_message='Not found dish in menu for delete')


@app.route('/orders/create', methods=['GET', 'POST'])
def create_order():
    global menu, order

    if request.method == 'POST':
        o = {
            'orderId': request.form['orderId'],
            'customerName': request.form['customerName'],
            'dishId': request.form['dishId'],
            'status': request.form['status']
        }
        print(o)
        dishId = int(request.form['dishId'])
        print(dishId)

        for dish in menu:
            if dish['id'] == int(dishId):
                if dish['availability'] == "yes":
                    order.append(o)
                    # Send the updated order status to all connected clients
                    # socketio.emit('order_update', order, broadcast=True)
                    return redirect('/orders')
                else:
                    return render_template('error.html', error_message='Sorry, Dish is not available!')
            else:
                return render_template('error.html', error_message='Not able to create Order, Not found dish in menu!')
    else:
        return render_template('create_order.html')


@app.route('/orders/update/<int:order_id>', methods=['GET', 'POST'])
def update_order(order_id):
    global order
    if request.method == "POST":
        newStatus = request.form['status']
        for o in order:
            if int(o['orderId']) == int(order_id):
                o['status'] = newStatus
                # Send the updated order status to all connected clients
                # socketio.emit('order_update', order, broadcast=True)
                return redirect('/orders')
    else:
        for o in order:
            if int(o['orderId']) == int(order_id):
                return render_template('update_order.html', o=o)


@app.route('/orders', methods=['GET'])
def list_orders():
    global order
    print(order)
    return render_template('orders.html', orders=order)


if __name__ == '__main__':
    # socketio.run(app, debug=True, port=8000)
    app.run(debug=True)

