from flask import Flask, render_template, request
from flask import url_for, redirect
from tmdb_client import get_popular_movies
import tmdb_client
import random

app = Flask(__name__)

app.secret_key = b'najtajniejszy_klucz'

FAVORITES = set()

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    available_lists = ['popular', 'now_playing', 'top_rated', 'upcoming']
    if selected_list not in available_lists:
        selected_list = 'popular'
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, movies_lists = available_lists)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast_details = tmdb_client.get_single_movie_cast(movie_id)
    images = tmdb_client.get_movie_images(movie_id)
    image = random.choice(images['backdrops'])
    return render_template("movie_details.html", movie=details, cast = cast_details, image = image)

@app.route("/search")
def search():
    query = request.args.get('q', '')
    results = tmdb_client.search(query)
    return render_template("search.html", results = results, query = query)

@app.route("/airing_today")
def airing_today():
    results = tmdb_client.airing()
    return render_template("airing_today.html", results = results)

@app.route("/favorites/add", methods=['POST'])
def add_to_favorites():
    movie_id = request.form.get('movie_id')
    if movie_id:
        FAVORITES.add(movie_id)
    return redirect(url_for('homepage'))

@app.route("/favorites")
def show_favorites():
    favorites = [tmdb_client.get_single_movie(movie_id) for movie_id in FAVORITES]
    return render_template("favorites.html", favorites = favorites)


if __name__ == '__main__':
    app.run(debug=True)

