CREATE TABLE airline(
airline_id integer PRIMARY KEY,
airline_code text,
airline_name text);

CREATE TABLE aircraft(
aircraft_id integer PRIMARY KEY,
airline_id integer REFERENCES airline,
aircraft_type text,
capacity integer);

CREATE TABLE airport(
airport_id integer PRIMARY KEY,
airline_id integer REFERENCES airline,
airport_code text,
city text,
state text);

CREATE TABLE flight(
flight_id integer PRIMARY KEY,
airline_id integer REFERENCES airline,
aircraft_id integer REFERENCES aircraft,
from_destination integer REFERENCES airport,
to_destination integer REFERENCES airport,
departure_date date,
departure_time time,
arrival_date date,
arrival_time time);

CREATE TABLE userprofile(
user_id integer PRIMARY KEY,
first_name text,
last_name text,
email text,
phone text,
street text,
street_number integer,
city text,
zip text);

CREATE TABLE account(
account_ID integer PRIMARY KEY,
user_id integer REFERENCES userprofile,
user_type text,
login_name text,
password text);

CREATE TABLE creditcard(
card_id integer PRIMARY KEY,
user_id integer REFERENCES userprofile,
card_type text,
card_number integer,
expirtation_month integer,
expiration_year integer);

CREATE TABLE booking(
book_id integer PRIMARY KEY,
flight_id integer REFERENCES flight,
user_id integer REFERENCES userprofile,
book_date date,
seats text,
class_ text,
price numeric);
