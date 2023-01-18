import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YWI0NjNlMzk1NjVjMDcyOGQ3ZGZmMGIxNjUwZWI4YyIsInN1YiI6IjYzYzY2YmEyYzUxYWNkMDA5MTZjNGNkNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aU1qZxlNFtHMbU1f9m3xwAUpqjAIKCldfA9DKkGpZJU"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(path, size="w342"):
    domain = "https://image.tmdb.org/t/p/"
    url = domain+size+path
    return url

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

