CREATE TABLE airline(
airlineID integer PRIMARY KEY,
airlineCode text,
airlineName text);

CREATE TABLE aircraft(
aircraftID integer PRIMARY KEY,
airlineID integer REFERENCES airline,
aircraftType text,
capacity integer);

CREATE TABLE airport(
airportID integer PRIMARY KEY,
airlineID integer REFERENCES airline,
airportCode text,
city text,
state text);

CREATE TABLE flight(
flightID integer PRIMARY KEY,
airlineID integer REFERENCES airline,
aircraftID integer REFERENCES aircraft,
fromDestination integer REFERENCES airport,
toDestination integer REFERENCES airport,
departureDate date,
departureTime time,
arrivalDate date,
arrivalTime time,
duration time);

CREATE TABLE userprofile(
userID integer PRIMARY KEY,
firstName text,
lastName text,
email text,
phone text,
street text,
streetNumber integer,
city text,
zip text);

CREATE TABLE account(
accountID integer PRIMARY KEY,
userID integer REFERENCES userprofile,
userType text,
loginName text,
password text);

CREATE TABLE creditcard(
cardID integer PRIMARY KEY,
userID integer REFERENCES userprofile,
cardType text,
cardNumber integer,
expirtationMonth integer,
expirationYear integer);

CREATE TABLE booking(
bookID integer PRIMARY KEY,
flightID integer REFERENCES flight,
userID integer REFERENCES userprofile,
bookDate date,
seats text,
class text,
price numeric);
