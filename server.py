"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, 
                    redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/homepage')
def homepage():
    """Display Homepage"""

    return render_template('homepage.html')


@app.route('/movies')
def view_movies():
    movies = crud.return_all_movies()

    return render_template('all_movies.html', movies=movies)
    

@app.route('/movies/<movie_id>')
def show_movie_details(movie_id):

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)

@app.route('/users')
def show_all_users():
    
    users = crud.return_all_users()
    
    return render_template('users.html', users=users)

@app.route('/users', methods=["POST"])
def register_user():
    """creates a new user"""
    
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash("This email already exists, please try to sign in")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash('Account successfully created')
    return redirect('/homepage')

@app.route('/login', methods=['POST'])
def handle_login():

    email = request.form.get('email')
    password = request.form.get('password')
    print("*"*10)
    print(email, password)
    print(request.form)
    user = crud.get_user_by_email(email)
    print(user.password)
    if password == user.password:
        print("I am here")
        session['user'] = user.user_id
        flash('Logging in!')
    else:
        flash('I\'m here')

    return redirect('/homepage')


    
@app.route('/users/<user_id>')
def show_user_details(user_id):

    user = crud.return_user_by_id(user_id)

    return render_template("user_details.html", user=user)




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)