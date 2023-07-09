from flask import Flask, render_template, request, redirect
app = Flask(__name__)

data = {}

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        data[name] = address
    return render_template('create.html')


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        if name in data:
            data[name] = address
    return render_template('update.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        name = request.form['name']
        if name in data:
            del data[name]
    return render_template('delete.html')


@app.route('/read')
def read():
    return render_template('read.html', data=data)


if __name__ == '__main__':
    app.run()