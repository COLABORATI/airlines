from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class Airline(db.Model):
    __tablename__ = 'airline'

    airline_id = db.Column(db.Integer, primary_key=True)
    airline_code = db.Column(db.String)
    airline_name = db.Column(db.String)

    def __init__(self, airline_code, airline_name):
        self.airline_code = airline_code
        self.airline_name = airline_name

class Airport(db.Model):
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
    __tablename__ = 'flight'

    flight_id = db.Column(db.Integer, primary_key=True)
    airline_id = db.Column(db.Integer, db.ForeignKey('airline.airline_id'))
    airline = db.relationship('Airline', backref=db.backref('flight', order_by=flight_id))
    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircraft.aircraft_id'))
    aircraft = db.relationship('Aircraft', backref=db.backref('flight', order_by=flight_id))
    fromdestination = db.Column(db.Integer, db.ForeignKey('airport.airport_id'))
    todestination = db.Column(db.Integer, db.ForeignKey('airport.airport_id'))
    fromdest = db.relationship('Airport',backref=db.backref('fromDest', order_by=flight_id), foreign_keys=[fromdestination])
    todest = db.relationship('Airport',backref=db.backref('toDest', order_by=flight_id), foreign_keys=[todestination])
    departuredate = db.Column(db.DateTime)
    departuretime = db.Column(db.DateTime)
    arrivaldate = db.Column(db.DateTime)
    arrivaltime = db.Column(db.DateTime)

    def __init__(self, departuredate, departuretime, arrivaldate, arrivaltime):
        self.departuredate = departuredate
        self.departuretime = departuretime
        self.arrivaldate = arrivaldate
        self.arrivaltime = arrivaltime

class UserProfile(db.Model):
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










