"""Describing the database tables with classes that will be mapped to tables"""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class Airline(db.Model):
    """Mapped class airline"""

    __tablename__ = 'airline'

    airline_id = db.Column(db.Integer, primary_key=True)
    airline_code = db.Column(db.String)
    airline_name = db.Column(db.String)

    def __init__(self, airline_code, airline_name):
        self.airline_code = airline_code
        self.airline_name = airline_name

class Airport(db.Model):
    """Mapped classs airport"""

    __tablename__ = 'airport'

    airport_id = db.Column(db.Integer, primary_key=True)
    airline_id = db.Column(db.Integer, db.ForeignKey('airline.airline_id'))
    airline = db.relationship('Airline', backref=db.backref('airport', order_by=airport_id))
    airport_code = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    
    def __init__(self, airport_code, city, state):
        self.airport_code = airport_code
        self.city = city
        self.state = state

class Aircraft(db.Model):
    """Mapped class aircraft"""

    __tablename__ = 'aircraft'

    aircraft_id = db.Column(db.Integer, primary_key=True)
    airline_id = db.Column(db.Integer, db.ForeignKey('airline.airline_id'))
    airline = db.relationship('Airline', backref=db.backref('aircraft', order_by=aircraft_id))
    aircraft_type = db.Column(db.String)
    capacity = db.Column(db.Integer)

    def __init__(self, aircraft_type, capacity):
        self.aircraft_type = aircraft_type
        self.capacity = capacity

class Flight(db.Model):
    """Mapped Class Flight"""

    __tablename__ = 'flight'

    flight_id = db.Column(db.Integer, primary_key=True)
    airline_id = db.Column(db.Integer, db.ForeignKey('airline.airline_id'))
    airline = db.relationship('Airline', backref=db.backref('flight', order_by=flight_id))
    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircraft.aircraft_id'))
    aircraft = db.relationship('Aircraft', backref=db.backref('flight', order_by=flight_id))
    from_destination = db.Column(db.Integer, db.ForeignKey('airport.airport_id'))
    to_destination = db.Column(db.Integer, db.ForeignKey('airport.airport_id'))
    from_dest = db.relationship('Airport',backref=db.backref('from_dest', order_by=flight_id), foreign_keys=[from_destination])
    to_dest = db.relationship('Airport',backref=db.backref('to_dest', order_by=flight_id), foreign_keys=[to_destination])
    departure_date = db.Column(db.DateTime)
    departure_time = db.Column(db.DateTime)
    arrival_date = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)

    def __init__(self, flight_id, airline_id, aircraft_id,
            from_destination, to_destination, departure_date,
            departure_time, arrival_date, arrival_time):
        self.flight_id = flight_id
        self.airline_id = airline_id
        self.aircraft_id = aircraft_id
        self.from_destination = from_destination
        self.to_destination = to_destination
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.arrival_date = arrival_date
        self.arrival_time = arrival_time

class UserProfile(db.Model):
    """Mapped Class User Profile"""

    __tablename__ = 'userprofile'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    street = db.Column(db.String)
    street_number = db.Column(db.Integer)
    city = db.Column(db.String)
    zip_code = db.Column(db.String)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)

    def __init__(self, first_name, last_name, email, phone, street, street_number, city, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.street = street
        self.street_number = street_number
        self.city = city
        self.zip_code = zip_code

class Account(db.Model):
    """Mapped Class Account"""

    __tablename__ = 'account'

    account_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('userprofile.user_id'))
    user = db.relationship('UserProfile', backref=db.backref('account', order_by=account_id))
    user_type = db.Column(db.String)
    login_name = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, user_type, login_name, password):
        self.user_type = user_type
        self.login_name = login_name
        self.password = password

class CreditCard(db.Model):
    """Mapped Class Credit Card"""

    __tablename__ = 'creditcard'

    card_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('userprofile.user_id'))
    user = db.relationship('UserProfile', backref=db.backref('creditcard', order_by=card_id))
    card_type = db.Column(db.String)
    card_number = db.Column(db.Integer)
    expiration_month = db.Column(db.Integer)
    expiration_year = db.Column(db.Integer)

    def __init__(self, card_type, card_number, expiration_month, expiration_year):
        self.card_type = card_type
        self.card_number = card_number
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year

class Booking(db.Model):
    """Mapped Class Booking"""

    __tablename__ = 'booking'

    book_id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.flight_id'))
    flight = db.relationship('Flight', backref=db.backref('booking', order_by=book_id))
    user_id = db.Column(db.Integer, db.ForeignKey('userprofile.user_id'))
    user = db.relationship('UserProfile', backref=db.backref('booking', order_by=book_id))
    book_date = db.Column(db.DateTime)
    seats = db.Column(db.String)
    class_ = db.Column(db.String)
    price = db.Column(db.Float)

    def __init__(self, book_date, seats, class_, price):
        self.book_date = book_date
        self.seats = seats
        self.class_ = class_
        self.price = price










