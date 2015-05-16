from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class Airline(db.Model):
    __tablename__ = 'airline'

    airlineID = db.Column(db.Integer, primary_key=True)
    airlineCode = db.Column(db.String)
    airlineName = db.Column(db.String)

    def __init__(self, airlineCode, airlineName):
        self.airlineCode = airlineCode
        self.airlineName = airlineName

class Airport(db.Model):
    __tablename__ = 'airport'

    airportID = db.Column(db.Integer, primary_key=True)
    airlineID = db.Column(db.Integer, db.ForeignKey('airline.airlineID'))
    airline = db.relationship('airline', backref=backref('airport', order_by=airportID))
    airportCode = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    
    def __init__(self, airportCode, city, state):
        self.airportCode = airportCode
        self.city = city
        self.state = state

class Aircraft(db.Model):
    __tablename__ = 'aircraft'

    aircraftID = db.Column(db.Integer, primary_key=True)
    airlineID = db.Column(db.Integer, db.ForeignKey('airline.airlineID'))
    airline = db.relationship('airline', backref=backref('aircraft', order_by=aircraftID))
    aircrafttype = db.Column(db.String)
    capacity = db.Column(db.Integer)

    def __init__(self, aircrafttype, capacity):
        self.aircrafttype = aircrafttype
        self.capacity = capacity

class Flight(db.Model):
    __tablename__ = 'flight'

    flightID = db.Column(db.Integer, primary_key=True)
    airlineID = db.Column(db.Integer, db.ForeignKey('airline.airlineID'))
    airline = db.relationship('airline', backref=backref('flight', order_by=flightID))
    aircraftID = db.Column(db.Integer, db.ForeignKey('aircraft.aircraftID'))
    aircraft = db.relationship('aircraft', backref=backref('flight', order_by=flightID))
    fromDestination = db.Column(db.Integer, db.ForeignKey('airport.airportID'))
    toDestination = db.Column(db.Integer, db.ForeignKey('airport.airportID'))
    airport = db.relationship('airport', backref=backref('flight', order_by=flightID))
    departureDate = datetime
    departureTime = datetime
    arrivalDate = datetime
    arrivalTime = datetime
    duration = datetime

    def __init__(self, departureDate, departureTime, arrivalDate, arrivalTime, duration):
        self.departureDate = departureDate
        self.departureTime = departureTime
        self.arrivalDate = arrivalDate
        self.arrivalTime = arrivalTime
        self.duration = duration

class UserProfile(db.Model):
    __tablename__ = 'userprofile'

    userID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String)
    lastName = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    street = db.Column(db.String)
    streetNumber = db.Column(db.Integer)
    city = db.Column(db.String)
    zipcode = db.Column(db.String)

    def __init__(self, firstName, lastName, email, phone, street, streetNumber, city, zipcode):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.street = street
        self.streetNumber = streetNumber
        self.city = city
        self.zipcode = zipcode

class Account(db.Model):
    __tablename__ = 'account'

    accountID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('userprofile.userID'))
    user = db.relationship('userprofile', backref=backref('account', order_by=accountID))
    userType = db.Column(db.String)
    loginName = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, userType, loginName, password):
        self.userType = userType
        self.loginName = loginName
        self.password = password

class CreditCard(db.Model):
    __tablename__ = 'creditcard'

    cardID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('userprofile.userID'))
    user = db.relationship('userprofile', backref=backref('creditcard', order_by=cardID))
    cardType = db.Column(db.String)
    cardNumber = db.Column(db.Integer)
    expirationMonth = db.Column(db.Integer)
    expirationYear = db.Column(db.Integer)

    def __init__(self, cardType, cardNumber, expirationMonth, expirationYear):
        self.cardType = cardType
        self.cardNumber = cardNumber
        self.expirationMonth = expirationMonth
        self.expirationYear = expirationYear

class Booking(db.Model):
    __tablename__ = 'booking'

    bookID = db.Column(db.Integer, primary_key=True)
    flightID = db.Column(db.Integer, db.ForeignKye('flight.flightID'))
    flight = db.relationship('flight', backref=backref('booking', order_by=bookID))
    userID = db.Column(db.Integer, db.ForeignKey('userprofile.userID'))
    user = db.relationship('userprofile', backref=backref('booking', order_by=bookID))
    bookDate = datetime
    seats = db.Column(db.String)
    class_ = db.Column(db.String)
    price = db.Column(db.Float)

    def __init__(self, bookDate, seats, class_, price):
        self.bookDate = bookDate
        self.seats = seats
        self.class_ = class_
        self.price = price










