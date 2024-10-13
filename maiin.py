import requests
import random


def get_random_disney_character():
    page = random.randint(1, 7438)
    page_size = 1
    url = f'https://api.disneyapi.dev/character?pageSize={page_size}&page={page}'

    response = requests.get(url)

    if response.ok:
        data = response.json()
        character = data['data'][0]

        print(f"Ім'я: {character['name']}")
        print(f"Фільми: {', '.join(character.get('films', [])) or 'Немає'}")
        print(f"Короткометражки: {', '.join(character.get('shortFilms', [])) or 'Немає'}")
        print(f"Серіали: {', '.join(character.get('tvShows', [])) or 'Немає'}")
        print(f"Відеоігри: {', '.join(character.get('videoGames', [])) or 'Немає'}")

    else:
        print('Щось пішло не так...')
        print(f'{response.status_code=}')


get_random_disney_character()