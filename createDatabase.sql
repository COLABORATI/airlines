CREATE TABLE airline(
airlineID integer PRIMARY KEY,
airlineCode text,
airlineName text);

CREATE TABLE aircraft(
aircraftID integer PRIMARY KEY,
airlineID integer REFERENCES airline,
type text,
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
duration interval [HOUR TO MINUTE]);

CREATE TABLE user(
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
userID integer REFERENCES user,
userType text,
loginName text,
password text);

CREATE TABLE creditcard(
cardID integer PRIMARY KEY,
userID integer REFERENCES user,
cardType text,
cardNumber integer,
expirtationMonth interval [MONTH],
expirationYear interval [YEAR]);

CREATE TABLE booking(
bookID integer PRIMARY KEY,
flightID integer REFERENCES flight,
userID integer REFERENCES user,
bookDate date,
seats text,
class text,
price numeric);
