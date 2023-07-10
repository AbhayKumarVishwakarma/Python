from flask import Flask, jsonify, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # SQLite in-memory database for testing

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def hello():
    return jsonify(message='Hello, World!')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    return jsonify(message='Login successfully', submitted_email=email, submitted_password=password)


@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('data')
    return jsonify(message='Form submitted', submitted_data=data)


@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    message = request.form.get('message')

    # Logic to process the feedback and save it

    return jsonify(message='Feedback submitted successfully')


if __name__ == '__main__':
    app.run()
