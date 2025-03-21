import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '9bebea3d18b8193432d6648a5aad3753'
HEADER ={'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '23449'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id : TRAINER_ID'})
    assert response.status_code ==200