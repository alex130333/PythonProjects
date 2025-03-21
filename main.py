import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9bebea3d18b8193432d6648a5aad3753'
HEADER ={'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_photo = {
    "pokemon_id": "272709",
    "name": "floki",
    "photo_id": 2
}
body_pokeball = {
    "pokemon_id": "272709"
}

response_create = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_create = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_photo)
print(response_create.text)

response_create = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_create.text)