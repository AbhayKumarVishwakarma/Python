from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to first flask project.'

@app.route('/greet/<username>')
def greet_user(username):
    return 'Hello, ' + username


@app.route('/farewell/<username>')
def farewell_user(username):
    return f'Goodbye, {username}'

if __name__ == '__main__':
    app.run()