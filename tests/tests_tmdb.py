from main import app
import tmdb_client
from unittest.mock import Mock
import pytest





def test_get_single_movie(monkeypatch):
    mock_single_movie = {'test_key1': 'test_value1', 'test_key2': 'test_value2' }
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    single_movie = tmdb_client.get_single_movie(100)
    assert single_movie == mock_single_movie


def test_get_movie_images(monkeypatch):
    mock_movie_images = {'test_key1': 'test_value1', 'test_key2': 'test_value2' }
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie_images
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movie_images = tmdb_client.get_movie_images(50)
    assert movie_images == mock_movie_images


def test_get_single_movie_cast(monkeypatch):
    mock_single_movie_cast = {
  "id": 550,
  "cast": [
    {
      "adult": False,
      "gender": 2,
      "id": 819,
      "known_for_department": "Acting",
      "name": "Edward Norton",
      "original_name": "Edward Norton",
      "popularity": 7.861,
      "profile_path": "/5XBzD5WuTyVQZeS4VI25z2moMeY.jpg",
      "cast_id": 4,
      "character": "The Narrator",
      "credit_id": "52fe4250c3a36847f80149f3",
      "order": 0
    },
    {
      "adult": False,
      "gender": 2,
      "id": 287,
      "known_for_department": "Acting",
      "name": "Brad Pitt",
      "original_name": "Brad Pitt",
      "popularity": 20.431,
      "profile_path": "/cckcYc2v0yh1tc9QjRelptcOBko.jpg",
      "cast_id": 5,
      "character": "Tyler Durden",
      "credit_id": "52fe4250c3a36847f80149f7",
      "order": 1
    },
    {
      "adult": False,
      "gender": 1,
      "id": 1283,
      "known_for_department": "Acting",
      "name": "Helena Bonham Carter",
      "original_name": "Helena Bonham Carter",
      "popularity": 14.399,
      "profile_path": "/mW1NolxQmPE16Zg6zuWyZlFgOwL.jpg",
      "cast_id": 6,
      "character": "Marla Singer",
      "credit_id": "52fe4250c3a36847f80149fb",
      "order": 2
    },
    {
      "adult": False,
      "gender": 2,
      "id": 7470,
      "known_for_department": "Acting",
      "name": "Meat Loaf",
      "original_name": "Meat Loaf",
      "popularity": 2.67,
      "profile_path": "/k9tJGdMkzOe17YH2ZCQjNnX5YLz.jpg",
      "cast_id": 7,
      "character": "Robert \"Bob\" Paulson",
      "credit_id": "52fe4250c3a36847f80149ff",
      "order": 3
    },
    {
      "adult": False,
      "gender": 2,
      "id": 7499,
      "known_for_department": "Acting",
      "name": "Jared Leto",
      "original_name": "Jared Leto",
      "popularity": 7.845,
      "profile_path": "/ca3x0OfIKbJppZh8S1Alx3GfUZO.jpg",
      "cast_id": 30,
      "character": "Angel Face",
      "credit_id": "52fe4250c3a36847f8014a51",
      "order": 4
    },
    {
      "adult": False,
      "gender": 2,
      "id": 7471,
      "known_for_department": "Acting",
      "name": "Zach Grenier",
      "original_name": "Zach Grenier",
      "popularity": 2.829,
      "profile_path": "/fSyQKZO39sUsqY283GXiScOg3Hi.jpg",
      "cast_id": 31,
      "character": "Richard Chesler",
      "credit_id": "52fe4250c3a36847f8014a55",
      "order": 5
    },
    {
      "adult": False,
      "gender": 2,
      "id": 7497,
      "known_for_department": "Acting",
      "name": "Holt McCallany",
      "original_name": "Holt McCallany",
      "popularity": 4.303,
      "profile_path": "/a5ax2ICLrV6l0T74OSFvzssCQyQ.jpg",
      "cast_id": 32,
      "character": "The Mechanic",
      "credit_id": "52fe4250c3a36847f8014a59",
      "order": 6
    },
    {
      "adult": False,
      "gender": 2,
      "id": 7498,
      "known_for_department": "Acting",
      "name": "Eion Bailey",
      "original_name": "Eion Bailey",
      "popularity": 5.407,
      "profile_path": "/hKqfGq1sPhZdQOlto0bS3igFZdP.jpg",
      "cast_id": 33,
      "character": "Ricky",
      "credit_id": "52fe4250c3a36847f8014a5d",
      "order": 7
    },
    {
      "adult": False,
      "gender": 2,
      "id": 7472,
      "known_for_department": "Acting",
      "name": "Richmond Arquette",
      "original_name": "Richmond Arquette",
      "popularity": 2.797,
      "profile_path": "/qpKZQn71Fwk6Gm1WZHL9IpVmcyO.jpg",
      "cast_id": 34,
      "character": "Intern",
      "credit_id": "52fe4250c3a36847f8014a61",
      "order": 8
    },
    {
      "adult": False,
      "gender": 2,
      "id": 7219,
      "known_for_department": "Acting",
      "name": "David Andrews",
      "original_name": "David Andrews",
      "popularity": 4.348,
      "profile_path": "/36LEerIIN7gpG52mM3Ier7YWDbh.jpg",
      "cast_id": 35,
      "character": "Thomas",
      "credit_id": "52fe4250c3a36847f8014a65",
      "order": 9
    },
    {
      "adult": False,
      "gender": 1,
      "id": 68277,
      "known_for_department": "Acting",
      "name": "Christina Cabot",
      "original_name": "Christina Cabot",
      "popularity": 1.672,
      "profile_path": "/h1vwbOfITSvDvDq8E9MVvWqMYSr.jpg",
      "cast_id": 36,
      "character": "Group Leader",
      "credit_id": "52fe4250c3a36847f8014a69",
      "order": 10
    },
    {
      "adult": False,
      "gender": 2,
      "id": 956719,
      "known_for_department": "Acting",
      "name": "Tim DeZarn",
      "original_name": "Tim DeZarn",
      "popularity": 2.687,
      "profile_path": "/AmY8QpXyWUCOX4SewTVytjqD8rz.jpg",
      "cast_id": 37,
      "character": "Inspector Bird",
      "credit_id": "52fe4250c3a36847f8014a6d",
      "order": 11
    },
    {
      "adult": False,
      "gender": 2,
      "id": 59285,
      "known_for_department": "Acting",
      "name": "Ezra Buzzington",
      "original_name": "Ezra Buzzington",
      "popularity": 2.254,
      "profile_path": "/j3kJRKgQdHAMXvJUtPHXJsGGW5X.jpg",
      "cast_id": 38,
      "character": "Inspector Dent",
      "credit_id": "52fe4250c3a36847f8014a71",
      "order": 12
    },
    {
      "adult": False,
      "gender": 2,
      "id": 17449,
      "known_for_department": "Acting",
      "name": "Bob Stephenson",
      "original_name": "Bob Stephenson",
      "popularity": 2.695,
      "profile_path": "/AczLnt4baxBT4gqSroSjCqD7S9D.jpg",
      "cast_id": 39,
      "character": "Airport Security Officer",
      "credit_id": "52fe4250c3a36847f8014a75",
      "order": 13
    },
    {
      "adult": False,
      "gender": 2,
      "id": 56112,
      "known_for_department": "Acting",
      "name": "David Lee Smith",
      "original_name": "David Lee Smith",
      "popularity": 3.371,
      "profile_path": "/hktppGThiKu30lcGW9CicNuinhc.jpg",
      "cast_id": 40,
      "character": "Walter",
      "credit_id": "52fe4250c3a36847f8014a79",
      "order": 14
    },
    {
      "adult": False,
      "gender": 2,
      "id": 42824,
      "known_for_department": "Acting",
      "name": "Carl Ciarfalio",
      "original_name": "Carl Ciarfalio",
      "popularity": 0.732,
      "profile_path": "/yADROfK7uJkmd8p3GyjxH8WZqRL.jpg",
      "cast_id": 42,
      "character": "Lou's Body Guard",
      "credit_id": "52fe4250c3a36847f8014a81",
      "order": 15
    },
    {
      "adult": False,
      "gender": 2,
      "id": 40277,
      "known_for_department": "Writing",
      "name": "Stuart Blumberg",
      "original_name": "Stuart Blumberg",
      "popularity": 1.4,
      "profile_path": None,
      "cast_id": 43,
      "character": "Car Salesman",
      "credit_id": "52fe4251c3a36847f8014a85",
      "order": 16
    },
    {
      "adult": False,
      "gender": 2,
      "id": 122805,
      "known_for_department": "Acting",
      "name": "Mark Fite",
      "original_name": "Mark Fite",
      "popularity": 1.435,
      "profile_path": "/qUbqKE14GAUdRhYqNcGzDkt1yi9.jpg",
      "cast_id": 44,
      "character": "Second Man at Auto Shop",
      "credit_id": "52fe4251c3a36847f8014a89",
      "order": 17
    },
    {
      "adult": False,
      "gender": 2,
      "id": 35521,
      "known_for_department": "Acting",
      "name": "Matt Winston",
      "original_name": "Matt Winston",
      "popularity": 2.556,
      "profile_path": "/et38vhCb9y8yGleMRNY2j4nDDyr.jpg",
      "cast_id": 45,
      "character": "Seminary Student",
      "credit_id": "52fe4251c3a36847f8014a8d",
      "order": 18
    },
    {
      "adult": False,
      "gender": 1,
      "id": 1224996,
      "known_for_department": "Acting",
      "name": "Lauren Sánchez",
      "original_name": "Lauren Sánchez",
      "popularity": 1.4,
      "profile_path": "/ahOwHtOHrFZUoJDOd7VvF7RPiL.jpg",
      "cast_id": 46,
      "character": "Channel 4 Reporter",
      "credit_id": "52fe4251c3a36847f8014a91",
      "order": 19
    },
    {
      "adult": False,
      "gender": 0,
      "id": 1219497,
      "known_for_department": "Acting",
      "name": "Thom Gossom Jr.",
      "original_name": "Thom Gossom Jr.",
      "popularity": 1.22,
      "profile_path": "/plFARWSTQ021TOOC5gpChhiUIVu.jpg",
      "cast_id": 41,
      "character": "Detective Stern",
      "credit_id": "52fe4250c3a36847f8014a7d",
      "order": 20
    },
    {
      "adult": False,
      "gender": 2,
      "id": 1226835,
      "known_for_department": "Acting",
      "name": "Markus Redmond",
      "original_name": "Markus Redmond",
      "popularity": 1.166,
      "profile_path": None,
      "cast_id": 52,
      "character": "Detective Kevin",
      "credit_id": "52fe4251c3a36847f8014aa9",
      "order": 21
    },
    {
      "adult": False,
      "gender": 2,
      "id": 41352,
      "known_for_department": "Acting",
      "name": "Van Quattro",
      "original_name": "Van Quattro",
      "popularity": 1.566,
      "profile_path": None,
      "cast_id": 51,
      "character": "Detective Andrew",
      "credit_id": "52fe4251c3a36847f8014aa5",
      "order": 22
    },
    {
      "adult": False,
      "gender": 0,
      "id": 177175,
      "known_for_department": "Acting",
      "name": "Michael Girardin",
      "original_name": "Michael Girardin",
      "popularity": 1.096,
      "profile_path": None,
      "cast_id": 84,
      "character": "Detective Walker",
      "credit_id": "588651eac3a3684628003490",
      "order": 23
    },
    {
      "adult": False,
      "gender": 2,
      "id": 109100,
      "known_for_department": "Acting",
      "name": "David Jean Thomas",
      "original_name": "David Jean Thomas",
      "popularity": 1.42,
      "profile_path": None,
      "cast_id": 47,
      "character": "Policeman",
      "credit_id": "52fe4251c3a36847f8014a95",
      "order": 24
    },
    {
      "adult": False,
      "gender": 0,
      "id": 1221838,
      "known_for_department": "Acting",
      "name": "Paul Carafotes",
      "original_name": "Paul Carafotes",
      "popularity": 2.188,
      "profile_path": None,
      "cast_id": 48,
      "character": "Salvator - Winking Bartender",
      "credit_id": "52fe4251c3a36847f8014a99",
      "order": 25
    },
    {
      "adult": False,
      "gender": 2,
      "id": 145531,
      "known_for_department": "Acting",
      "name": "Christopher John Fields",
      "original_name": "Christopher John Fields",
      "popularity": 1.817,
      "profile_path": "/3ASDmbBZQnk526pPeNtb8LOJXBX.jpg",
      "cast_id": 49,
      "character": "Proprietor of Dry Cleaners",
      "credit_id": "52fe4251c3a36847f8014a9d",
      "order": 26
    },
    {
      "adult": False,
      "gender": 2,
      "id": 9291,
      "known_for_department": "Acting",
      "name": "Michael Shamus Wiles",
      "original_name": "Michael Shamus Wiles",
      "popularity": 1.62,
      "profile_path": "/niY4gYqAUjmnU4KRiguxpsKliWA.jpg",
      "cast_id": 50,
      "character": "Bartender in Halo",
      "credit_id": "52fe4251c3a36847f8014aa1",
      "order": 27
    }]}
    requests_mock = Mock()
    response= requests_mock.return_value
    response.json.return_value = mock_single_movie_cast
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    single_movie_cast = tmdb_client.get_single_movie_cast(150)
    assert single_movie_cast == mock_single_movie_cast['cast']


@pytest.mark.parametrize('list_type',('popular','top_rated','upcoming','now_playing'))
def test_homepage(monkeypatch, list_type):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get(f"/?list_type={list_type}")
       assert response.status_code == 200
       api_mock.assert_called_with(f"movie/{list_type}")
       print(api_mock.call_args)










"""def test_homepage2(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular')"""