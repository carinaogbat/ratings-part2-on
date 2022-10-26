"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def return_all_users():
    """"Return a list of all users"""

    return User.query.all()

def return_user_by_id(user_id):
    """"Returns a user by their ID"""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by their email, else returns None"""

    return User.query.filter(User.email == email).first()

def get_user_password(password):
    """Return User password"""

    return User.query.filter(User.password == password).first()


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    return movie


def return_all_movies():
    """"Return a list of all movies"""
    
    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Return a movie by it's ID"""

    return Movie.query.get(movie_id)

def create_rating(user, movie, score):
    """Creates and returns a user rating"""

    rating = Rating(user=user, movie=movie, score=score)

    return rating



    

    
if __name__ == '__main__':
    from server import app
    connect_to_db(app)