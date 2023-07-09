from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "3492Abhay@gmail.com"
app.config['MYSQL_DB'] = "flask_db"

mysql = MySQL(app)


@app.route('/')
def index():
    return 'Welcome to Zomato Chronicles!'


@app.route('/dishes/create', methods=['GET', 'POST'])
def create_dish():
    if request.method == 'POST':
        dishId = request.form['id']
        name = request.form['name']
        price = request.form['price']
        availability = request.form['available']

        cur = mysql.connection.cursor()
        cur.execute("insert into menu (dishId, name, price, availability) values (%s, %s, %s, %s)", (dishId, name, price, availability))
        mysql.connection.commit()
        cur.close()
        return redirect('/dishes')
    else:
        return render_template('add_dish.html')


@app.route('/dishes', methods=['GET'])
def list_dishes():
    cur = mysql.connection.cursor()
    allData = cur.execute("select * from menu")
    if allData > 0:
        dishes = cur.fetchall()
        cur.close()
        return render_template('dishes.html', dishes=dishes)
    else:
        return render_template('error.html', error_message='Not found any dish in menu')


@app.route('/dishes/update/<int:dish_id>', methods=['GET', 'POST'])
def update_dish(dish_id):
    cur = mysql.connection.cursor()
    data = cur.execute("select * from menu where dishId = %s", (dish_id,))
    if data > 0:
        dish = cur.fetchone()
    else:
        return render_template('error.html', error_message='Not found dish in menu')

    if request.method == 'POST':
        available = request.form['available']
        cur.execute("UPDATE menu SET availability = %s WHERE dishId = %s", (available, dish_id))
        mysql.connection.commit()
        cur.close()
        return redirect('/dishes')
    else:
        if int(dish[0]) == int(dish_id):
            return render_template('update_dish.html', dish=dish)


@app.route('/dishes/delete/<int:dish_id>')
def delete_dish(dish_id):
    cur = mysql.connection.cursor()
    data = cur.execute("select * from menu where dishId = %s", (dish_id,))
    if data > 0:
        dish = cur.fetchone()
    else:
        return render_template('error.html', error_message='Not found any dish in menu')

    cur.execute("DELETE FROM menu WHERE dishId = %s", (dish_id,))
    mysql.connection.commit()
    cur.close()
    print(f"deleted data -> {dish}")
    return redirect('/dishes')


@app.route('/orders/create', methods=['GET', 'POST'])
def create_order():
    if request.method == 'POST':
        orderId = request.form['orderId']
        customerName = request.form['customerName']
        dishId = request.form['dishId']
        status = request.form['status']

        cur = mysql.connection.cursor()
        data = cur.execute("SELECT * FROM menu WHERE dishId = %s", (dishId,))
        if data > 0:
            dish = cur.fetchone()
        else:
            return render_template('error.html', error_message='Sorry, Not found dish')

        print("dish id " + dishId)

        if dish[3] == "yes":
            cur.execute("INSERT INTO orders (orderId, customerName, dishId, status) VALUES (%s, %s, %s, %s)", (orderId, customerName, dishId, status))
            mysql.connection.commit()
            cur.close()
            return redirect('/orders')
        else:
            cur.close()
            return render_template('error.html', error_message='Sorry, this dish is not available')
    else:
        return render_template('create_order.html')


@app.route('/orders/update/<int:order_id>', methods=['GET', 'POST'])
def update_order(order_id):
    cur = mysql.connection.cursor()
    data = cur.execute("select * from orders where orderId = %s", (order_id,))
    if data > 0:
        order = cur.fetchone()
    else:
        return render_template('error.html', error_message='Not found any dish in menu')

    if request.method == "POST":
        newStatus = request.form['status']
        cur.execute("UPDATE orders SET status = %s WHERE orderId = %s", (newStatus, order_id))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    else:
        cur.close()
        return render_template('update_order.html', order=order)


@app.route('/orders', methods=['GET'])
def list_orders():
    cur = mysql.connection.cursor()
    data = cur.execute("select * from orders")
    if data > 0:
        orders = cur.fetchall()
        cur.close()
        return render_template('orders.html', orders=orders)
    else:
        cur.close()
        return render_template('error.html', error_message='Not found any dish in menu')


if __name__ == '__main__':
    app.run(debug=True)
