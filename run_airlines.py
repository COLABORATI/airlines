from models import Flights, app, db
from flask import Flask, request, flash, url_for, redirect, render_template, abort, session
from flask_sqlalchemy import SQLAlchemy


@app.route('/')
def show_all():
    return render_template('show_all.html', flights=Flights.query.order_by(Flights.id.desc()).all())

@app.route('/show_flight/<flight_id>', methods=['GET', 'POST'])
def show_flight(flight_id):
    return render_template('show_flight.html', flight_=Flights.query.filter(Flights.id==flight_id))

@app.route('/search_flight/<flight_num>', methods=['GET', 'POST'])
def search_flight(flight_num):
    return render_template('search_flight.html', flight_=Flights.query.filter(Flights.flight_num==flight_num))

#SearchBox
#class SearchForm(Form):
    #search = IntegerField('search', validators=[DataRequired()])
    
#@app.route('/search', methods=('GET', 'POST'))
#def search():
    #form = SearchForm()
    #if form.validate_on_submit():
        #return redirect(url_for('show_all'))
    #return render_template('search.html', form=form.search.data)

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['flight_no']:
            flash('Flight number is required', 'error')
        elif not request.form['airline_name']:
            flash('Airline name is required', 'error')
        elif not request.form['flight_time']:
            flash('Time is required', 'error')
        elif not request.form['flight_date']:
            flash('date is required', 'error')
        elif not request.form['from_dest']:
            flash('From Destination is required', 'error')
        elif not request.form['to_dest']:
            flash('To destination is required', 'error')
        elif not request.form['gate_no']:
            flash('Gate is required', 'error')
        else:
            flight = Flights(request.form['flight_no'], request.form['airline_name'],request.form['flight_time'], request.form['flight_date'],request.form['from_dest'], request.form['to_dest'], request.form['gate_no'])
            db.session.add(flight)
            db.session.commit()
            flash(u'Flight successfully created')
            return redirect(url_for('show_all'))
    return render_template('new.html')

@app.route('/edit/<flight_id>', methods=['GET', 'POST'])
def edit(flight_id):
    flight_edit = Flights.query.get(flight_id)
    if flight_edit == None:
        flush('Flight does not exist')
        return redirect(url_for('show_all'))
    elif request.method == 'POST':
        flight_edit.flight_num = request.form['flight_number']
        flight_edit.airline_name = request.form['airline_name']
        flight_edit.time_time = request.form['time_time']
        flight_edit.date_date = request.form['date_date']
        flight_edit.from_dest = request.form['from_dest']
        flight_edit.to_dest = request.form['to_dest']
        flight_edit.gate_num = request.form['gate_num']
        db.session.commit()
        flash('Flight successfully edited')
        return redirect(url_for('show_all'))
    return render_template('edit.html', flight_edit=flight_edit)

@app.route('/delete/<flight_id>', methods=['GET', 'POST'])
def delete(flight_id):
    #delete_flight = Flights.query.filter(Flights.id==flight_id)
    delete_flight = Flights.query.get(flight_id)
    db.session.delete(delete_flight)
    flash('Flight Deleted')
    db.session.commit()
    return redirect(url_for('show_all'))
    

@app.route('/update', methods=['POST'])
def update_done():
    Flights.query.all()
    flash('Updated!')
    db.session.commit()
    return redirect(url_for('show_all'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid Username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Password'
        else:
            session['logged_in'] = True
            flash('You were log in!')
            return redirect(url_for('show_all'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_all'))



if __name__ == '__main__':
    app.run()

