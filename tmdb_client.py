import requests
api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YWI0NjNlMzk1NjVjMDcyOGQ3ZGZmMGIxNjUwZWI4YyIsInN1YiI6IjYzYzY2YmEyYzUxYWNkMDA5MTZjNGNkNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aU1qZxlNFtHMbU1f9m3xwAUpqjAIKCldfA9DKkGpZJU"



def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()


def get_popular_movies():
    return call_tmdb_api(f"movie/popular")

def get_movies_list(list_type = 'popular'):
    return call_tmdb_api(f"movie/{list_type}")
     

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type = 'popular'):  
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):    
    return call_tmdb_api(f"movie/{movie_id}")
    

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")['cast']


def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")
    

def search(search_query):
    endpoint = f"https://api.themoviedb.org/3/search/movie?query={search_query}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response = response.json()
    return response['results']

def airing():
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response = response.json()
    return response['results']