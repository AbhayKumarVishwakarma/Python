from app import app, db, User


def test_create_user():
    with app.app_context():
        db.create_all()  # creating the database

        user = User(username='test_user')
        db.session.add(user)
        db.session.commit()

        assert User.query.filter_by(username='test_user').first() is not None

        db.drop_all()  # deleting the database
