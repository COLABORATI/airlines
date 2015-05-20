from models import Flight, Airline, Airport, Aircraft, UserProfile, Account, CreditCard, Booking, app, db
from flask import Flask, request, flash, url_for, redirect, render_template, abort, session, escape
from flask_sqlalchemy import SQLAlchemy
@app.route('/')
def show_all():
    return render_template('show_all.html', flights=Flight.query.order_by(Flight.flight_id.desc()).all())

@app.route('/show_flight', methods=['GET', 'POST'])
def show_flight():
    return render_template('show_flight.html', flights=Flight.query.order_by(Flight.flight_id.desc()).all())

@app.route('/show_airport', methods=['GET', 'POST'])
def show_airport():
    return render_template('show_airport.html', airports=Airport.query.order_by(Airport.airport_id.desc()).all())

@app.route('/show_airline', methods=['GET', 'POST'])
def show_airline():
    return render_template('show_airline.html', airlines=Airline.query.order_by(Airline.airline_id.desc()).all())

@app.route('/show_aircraft', methods=['GET', 'POST'])
def show_aircraft():
    return render_template('show_aircraft.html', aircrafts=Aircraft.query.order_by(Aircraft.aircraft_id.desc()).all())

@app.route('/show_userprofile', methods=['GET', 'POST'])
def show_userprofile():
    return render_template('show_userprofile.html', users=UserProfile.query.order_by(UserProfile.user_id.desc()).all())

@app.route('/search_flight/<flight_id>', methods=['GET', 'POST'])
def search_flight(flight_id):
    return render_template('show_flight.html', flight=Flight.query.order_by(Flight.user_id==flight_id))

@app.route('/current_user/<user_id>', methods=['GET', 'POST'])
def current_user(user_id):
    return render_template('show_userprofile.html', users=UserProfile.query.filter(UserProfile.user_id==user_id))

#SearchBox
#class SearchForm(Form):
    #search = IntegerField('search', validators=[DataRequired()])
    
#@app.route('/search', methods=('GET', 'POST'))
#def search():
    #form = SearchForm()
    #if form.validate_on_submit():
        #return redirect(url_for('show_all'))
    #return render_template('search.html', form=form.search.data)

"""=================== NEW ==================="""


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['flight_id']:
            flash('Flight_id is required', 'error')
        elif not request.form['airline_id']:
            flash('airline_id is required', 'error')
        elif not request.form['aircraft_id']:
            flash('aircraftID is required', 'error')
        elif not request.form['from_destination']:
            flash('fromDestination is required', 'error')
        elif not request.form['to_destination']:
            flash('toDestination is required', 'error')
        elif not request.form['departure_date']:
            flash('departureDate is required', 'error')
        elif not request.form['departure_time']:
            flash('departureTime is required', 'error')
        elif not request.form['arrival_date']:
            flash('arrivalDate is required', 'error')
        elif not request.form['arrival_time']:
            flash('arrivalTime is required', 'error')
        else:
            flight = Flight(request.form['flight_id'],request.form['airline_id'], request.form['aircraft_id'],request.form['from_destination'], 
            request.form['to_destination'],request.form['departure_date'], request.form['departure_time'], 
            request.form['arrival_date'], request.form['arrival_time'])
            db.session.add(flight)
            db.session.commit()
            flash(u'Flight successfully created')
            return redirect(url_for('show_all'))
    return render_template('new.html')

@app.route('/new_flight', methods=['GET', 'POST'])
def new_airport():
    """Create new airport"""
    if request.method == 'POST':
        if not request.form['airport_id']:
            flash('airport_id is required', 'error')
        elif not request.form['airline_id']:
            flash('airline_id is required', 'error')
        elif not request.form['airport_code']:
            flash('airport_code is required', 'error')
        elif not request.form['city']:
            flash('city is required', 'error')
        elif not request.form['state']:
            flash('state is required', 'error')
        else:
            airport = Airport(request.form['airport_id'],request.form['airline_id'],
                    request.form['airport_code'], request.form['city'],
                    request.form['state'])
            db.session.add(airport)
            db.session.commit()
            flash(u'Airport successfully created')
            return redirect(url_for('show_airport'))
    return render_template('new_airport.html')

@app.route('/new_airline', methods=['GET', 'POST'])
def new_airline():
    """Create new airline"""
    if request.method == 'POST':
        if not request.form['airline_id']:
            flash('airline_id is required', 'error')
        elif not request.form['airline_code']:
            flash('airline_code is required', 'error')
        elif not request.form['airline_name']:
            flash('airline_name is required', 'error')
        else:
            airline = Airline(request.form['airline_id'], request.form['airline_code'],
                    request.form['airline_name'])
            db.session.add(airline)
            db.session.commit()
            flash(u'Airline successfully created')
            return redirect(url_for('show_airline'))
    return render_template('new_airline.html')

@app.route('/new_aircraft', methods=['GET', 'POST'])
def new_aircraft():
    """Create new airlie"""
    if request.method == 'POST':
        if not request.form['aircraft_id']:
            flash('aircraft_id is required', 'error')
        elif not request.form['airline_id']:
            flash('airline_id is required', 'error')
        elif not request.form['aircraft_type']:
            flash('aircraft_type is required', 'error')
        elif not request.form['capacity']:
            flash('capacity is required', 'error')
        else:
            aircraft = Aircraft(request.form['aircraft_id'], request.form['airline_id'],
                    request.form['aircraft_type'], request.form['capacity'])
            db.session.add(aircraft)
            db.session.commit()
            flash(u'Aircraft successfully created')
            return redirect(url_for('show_aircraft'))
    return render_template('new_aircraft.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register new user"""
    if request.method == 'POST':
        if not request.form['user_id']:
            flash('User_id is required', 'error')
        elif not request.form['first_name']:
            flash('First Name is required', 'error')
        elif not request.form['last_name']:
            flash('Last Name is required')
        elif not request.form['email']:
            flash('Email is required', 'error')
        elif not requst.form['phone']:
            flash('Phone number is required', 'error')
        elif not request.form['street']:
            flash('Street is required', 'error')
        elif not request.form['street_number']:
            flash('Number is required', 'error')
        elif not request.form['city']:
            flash('City is required', 'error')
        elif not request.form['zip_code']:
            flash('ZIP code is required', 'error')
        else:
            user = UserProfile(request.form['user_id'], request.form['first_name'],
                    request.form['last_name'], request.form['email'], request.form['phone'],
                    request.form['street'],request.form['steet_number'], request.form['city'],
                    request.form['zip_code'])
            db.session.add(user)
            db.session.commit()
            flash(u'Successfully registered')
            return redirect(url_for('show_userprofile'))
    return render_template('register_user.html')

"""=================== EDIT ==================="""


@app.route('/edit/<flight_id>', methods=['GET', 'POST'])
def edit(flight_id):
    flight_edit = Flight.query.get(flight_id)
    if flight_edit == None:
        flush('Flight does not exist')
        return redirect(url_for('show_all'))
    elif request.method == 'POST':
        flight_edit.airline_id = request.form['airline_id']
        flight_edit.aircraft_id = request.form['aircraft_id']
        flight_edit.from_destination = request.form['from_destination']
        flight_edit.to_destination = request.form['to_destination']
        flight_edit.departure_date = request.form['departure_date']
        flight_edit.departure_time = request.form['departure_time']
        flight_edit.arrival_date = request.form['arrival_date']
        flight_edit.arrival_time = request.form['arrival_time']
        db.session.commit()
        flash('Flight successfully edited')
        return redirect(url_for('show_flight'))
    return render_template('edit.html', flight_edit=flight_edit)

@app.route('/edit_airport/<airport_id>', methods=['GET', 'POST'])
def edit_airport(airport_id):
    """Edit method for editing airport"""
    airport_edit = Airport.query.get(airport_id)
    if airport_edit == None:
        flush('Airport does not exist')
        return redirect(url_for('show_airport'))
    elif request.method == 'POST':
        airport_edit.airport_code = request.form['airport_code']
        airport_edit.city = request.form['city']
        airport_edit.state = request.form['state']
        db.session.commit()
        flash('Airport successfully edited')
        return redirect(url_for('show_airport'))
    return render_template('edit_airport.html', airport_edit=airport_edit)

@app.route('/edit_airline/<airline_id>', methods=['GET', 'POST'])
def edit_airline(airline_id):
    """Edit method for editing airline"""
    airline_edit = Airline.query.get(airline_id)
    if airline_edit == None:
        flush('Airline does not exist')
        return redirect(url_for('show_airline'))
    elif request.method == 'POST':
        airline_edit.airline_code = request.form['airline_code']
        airline_edit.airline_name = request.form['airline_name']
        db.session.commit()
        flash('Airline successfully edited')
        return redirect(url_for('show_airline'))
    return render_template('edit_airline.html', airline_edit=airline_edit)

@app.route('/edit_aircraft/<aircraft_id>', methods=['GET', 'POST'])
def edit_aircraft(aircraft_id):
    """Edit method for editing airline"""
    aircraft_edit = Aircraft.query.get(aircraft_id)
    if aircraft_edit == None:
        flush('Aircraft does not exist')
        return redirect(url_for('show_aircraft'))
    elif request.method == 'POST':
        aircraft_edit.aircraft_type = request.form['aircraft_type']
        aircraft_edit.capacity = request.form['capacity']
        db.session.commit()
        flash('Aircraft successfully edited')
        return redirect(url_for('show_aircraft'))
    return render_template('edit_aircraft.html', aircraft_edit=aircraft_edit)

@app.route('/edit_user/<user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    """Edit method for editing airline"""
    user_edit = UserProfile.query.get(user_id)
    if user_edit == None:
        flush('Aircraft does not exist')
        return redirect(url_for('show_userprofile'))
    elif request.method == 'POST':
        user_edit.first_name = request.form['first_name']
        user_edit.last_name = request.form['last_name']
        user_edit.email = request.form['email']
        user_edit.phone = request.form['phone']
        user_edit.street = request.form['street']
        user_edit.street_number = request.form['street_number']
        user_edit.city = request.form['city']
        user_edit.zip_code = request.form['zip_code']
        db.session.commit()
        flash('Aircraft successfully edited')
        return redirect(url_for('show_userprofile'))
    return render_template('edit_user.html', user_edit=user_edit)

"""=================== DELETE ==================="""

@app.route('/delete/<flight_id>', methods=['GET', 'POST'])
def delete(flight_id):
    """Delete Flihgt"""

    delete_flight = Flight.query.get(flight_id)
    db.session.delete(delete_flight)
    flash('Flight Deleted')
    db.session.commit()
    return redirect(url_for('show_all'))
    

@app.route('/delete_airport/<airport_id>', methods=['GET', 'POST'])
def delete_airport(airport_id):
    """Method for deleting airport"""
    delete_airport = Airport.query.get(airport_id)
    db.session.delete(delete_airport)
    flash('Airport deleted!')
    db.session.commit()
    return redirect(url_for('show_airport'))

@app.route('/delete_airline/<airline_id>', methods=['GET', 'POST'])
def delete_airline(airline_id):
    """Method fior deleting airline"""
    delete_airline = Airline.query.get(airline_id)
    db.session.delete(delete_airline)
    flash('Airline deleted!')
    db.session.commit()
    return redirect(url_for('show_airline'))

@app.route('/delete_aircraft/<aircraft_id>', methods=['GET', 'POST'])
def delete_aircraft(airline_id):
    """Method for deleting aircraft"""
    delete_aircraft = Aircraft.query.get(aircraft_id)
    db.session.delete(delete_aircraft)
    flash('Airline deleted!')
    db.session.commit()
    return redirect(url_for('show_aircraft'))

@app.route('/delete_user/<user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    """Method for deleting users"""
    delete_user = UserProfile.query.get(user_id)
    db.session.delete(delete_user)
    flash('User deleted!')
    db.session.commit()
    return redirect(url_for('show_userprofile'))

@app.route('/update', methods=['POST'])
def update_done():
    """Update All Flight"""
    Flight.query.all()
    flash('Updated!')
    db.session.commit()
    return redirect(url_for('show_all'))

"""=================== LOGIN ==================="""

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = Account.query.filter(Account.login_name==request.form['username']).first()
        if not user:
            error = 'Invalid Username'
        elif request.form['password'] != user.password:
            error = 'Invalid Password'
        else:
            session['username'] = user.login_name
            session['id'] = user.user_id
            session['type'] = user.user_type
            session['logged_in'] = True
            flash('You were log in!')
            return redirect(url_for('show_all'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('id', None)
    session.pop('type', None)
    flash('You were logged out')
    return redirect(url_for('show_all'))


if __name__ == '__main__':
    app.run()

