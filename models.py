from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class Flights(db.Model):
    __tablename__ = 'flights'

    id = db.Column(db.Integer, primary_key=True)
    flight_no = db.Column(db.String)
    airline_name = db.Column(db.String)
    flight_time = db.Column(db.Time)
    flight_date = db.Column(db.Date)
    from_dest = db.Column(db.String)
    to_dest = db.Column(db.String)
    gate_no = db.Column(db.String)

    def __init__(self, flight_no, airline_name, flight_time, flight_date, from_dest, to_dest, gate_no):
        self.flight_no = flight_no
        self.airline_name = airline_name
        self.flight_time = flight_time
        self.flight_date = flight_date
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.gate_no = gate_no
