from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class Airline(db.Model):
    __tablename__ = 'airline'

    airlineid = db.Column(db.Integer, primary_key=True)
    airlineode = db.Column(db.String)
    airlinename = db.Column(db.String)

    def __init__(self, airlinecode, airlinename):
        self.airlinecode = airlinecode
        self.airlinename = airlinename

class Airport(db.Model):
    __tablename__ = 'airport'

    airportid = db.Column(db.Integer, primary_key=True)
    airlineid = db.Column(db.Integer, db.ForeignKey('airline.airlineid'))
    airline = db.relationship('Airline', backref=db.backref('airport', order_by=airportid))
    airportcode = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    
    def __init__(self, airporcode, city, state):
        self.airportcode = airportcode
        self.city = city
        self.state = state

class Aircraft(db.Model):
    __tablename__ = 'aircraft'

    aircraftid = db.Column(db.Integer, primary_key=True)
    airlineid = db.Column(db.Integer, db.ForeignKey('airline.airlineid'))
    airline = db.relationship('Airline', backref=db.backref('aircraft', order_by=aircraftid))
    aircrafttype = db.Column(db.String)
    capacity = db.Column(db.Integer)

    def __init__(self, aircrafttype, capacity):
        self.aircrafttype = aircrafttype
        self.capacity = capacity

class Flight(db.Model):
    __tablename__ = 'flight'

    flightid = db.Column(db.Integer, primary_key=True)
    airlineid = db.Column(db.Integer, db.ForeignKey('airline.airlineid'))
    airline = db.relationship('Airline', backref=db.backref('flight', order_by=flightid))
    aircraftid = db.Column(db.Integer, db.ForeignKey('aircraft.aircraftid'))
    aircraft = db.relationship('Aircraft', backref=db.backref('flight', order_by=flightid))
    fromdestination = db.Column(db.Integer, db.ForeignKey('airport.airportid'))
    todestination = db.Column(db.Integer, db.ForeignKey('airport.airportid'))
    fromdest = db.relationship('Airport',backref=db.backref('fromDest', order_by=flightid), foreign_keys=[fromdestination])
    todest = db.relationship('Airport',backref=db.backref('toDest', order_by=flightid), foreign_keys=[todestination])
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

    userid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    street = db.Column(db.String)
    streetnumber = db.Column(db.Integer)
    city = db.Column(db.String)
    zipcode = db.Column(db.String)

    def __init__(self, firstname, lastname, email, phone, street, streetnumber, city, zipcode):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.street = street
        self.streetnumber = streetnumber
        self.city = city
        self.zipcode = zipcode

class Account(db.Model):
    __tablename__ = 'account'

    accountid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userprofile.userid'))
    user = db.relationship('UserProfile', backref=db.backref('account', order_by=accountid))
    usertype = db.Column(db.String)
    loginname = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, usertype, loginname, password):
        self.usertype = usertype
        self.loginname = loginname
        self.password = password

class CreditCard(db.Model):
    __tablename__ = 'creditcard'

    cardid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userprofile.userid'))
    user = db.relationship('UserProfile', backref=db.backref('creditcard', order_by=cardid))
    cardtype = db.Column(db.String)
    cardnumber = db.Column(db.Integer)
    expirationmonth = db.Column(db.Integer)
    expirationyear = db.Column(db.Integer)

    def __init__(self, cardtype, cardnumber, expirationmonth, expirationyear):
        self.cardtype = cardtype
        self.cardnumber = cardnumber
        self.expirationmonth = expirationmonth
        self.expirationyear = expirationyear

class Booking(db.Model):
    __tablename__ = 'booking'

    bookid = db.Column(db.Integer, primary_key=True)
    flightid = db.Column(db.Integer, db.ForeignKey('flight.flightid'))
    flight = db.relationship('Flight', backref=db.backref('booking', order_by=bookid))
    userid = db.Column(db.Integer, db.ForeignKey('userprofile.userid'))
    user = db.relationship('UserProfile', backref=db.backref('booking', order_by=bookid))
    bookdate = db.Column(db.DateTime)
    seats = db.Column(db.String)
    class_ = db.Column(db.String)
    price = db.Column(db.Float)

    def __init__(self, bookdate, seats, class_, price):
        self.bookdate = bookdate
        self.seats = seats
        self.class_ = class_
        self.price = price










