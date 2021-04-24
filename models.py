from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
 

# MODELS GO BELOW
class User(db.Model):
    """User model"""

    __tablename__ = "users"

    # make it easier to see object details
    def __repr__(self):
        return f"<User id={self.id} username={self.username}"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #email = db.Column(db.Text, nullable=False, unique=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    

    @classmethod
    def signup(cls, username, email, pwd, image_url):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(pwd).decode('UTF-8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            image_url=image_url,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, pwd):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        u = User.query.filter_by(username=username).first()

        # u.password = crazy long string in database, pwd = what user typed into form
        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance (aka <User 3>)
            return u
        else:
            return False


class Stock(db.Model):
    """Stocks Model"""

    __tablename__ = "stocks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner = db.Column(db.Integer, db.ForeignKey('users.id'))
    company_name = db.Column(db.Text, nullable=False, unique=True)
    ticker_symbol = db.Column(db.Text, nullable=False, unique=True)
    price = db.Column(db.Float)