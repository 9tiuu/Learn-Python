
import mysql.connector
import requests

DB_CONFIG = { # Datos de la DB (phpMyAdmin)
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'pokemon'
}

class Pokemon:
    def __init__(self, poke_id, name, height, weight, types):
        self.poke_id = poke_id
        self.name = name
        self.height = height
        self.weight = weight
        self.types = types

def create_http_request(poke_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{poke_id}' # URL de los datos del pokemon (API json)
    respuesta = requests.get(url)

    json_data = respuesta.json()
    return json_data

def create_pokemon_object(json_data):
    types = json_data['types'][0]['type']['name'] if json_data['types'] else None

    pokemon = Pokemon ( # Datos de la API
        poke_id=json_data['id'],
        name=json_data['name'],
        height=json_data['height'],
        weight=json_data['weight'],
        types=types
    )

    return pokemon

def save_to_database(pokemon): # Funcion para conectar a la DB y crear una tabla e insertar datos
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:

            # Crear tabla "pokemons" en caso de que no exista dentro de la DB seleccionada
            cursor.execute(''' 
                           CREATE TABLE IF NOT EXISTS pokemons (pokemon_id INT PRIMARY KEY, name VARCHAR(255), height INT, weight INT, types TEXT)
                        ''')

            # Consulta SQL para agregar los datos obtenidos desde la API y expecificadas en el objeto creado         
            cursor.execute('''
                           INSERT INTO pokemons (pokemon_id, name, height, weight, types) VALUES (%s, %s, %s, %s, %s)
                           ''', (pokemon.poke_id, pokemon.name, pokemon.height, pokemon.weight, str(pokemon.types)))
            
            connection.commit()

def list_pokemons(): # Funcion para conectar a la DB y realizar un listado para luego mostrarlos por consola
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:       

            cursor.execute('SELECT * FROM pokemons') # Consulta SQL para listar los datos registrados en la base de datos
            pokemons = cursor.fetchall()

            print('\n==== Lista de Pokemones agregados en la DB ====')

            for pokemon in pokemons:
                print(f'\n- ID: {pokemon[0]}')
                print(f'- Nombre: {pokemon[1]}')
                print(f'- Altura: {pokemon[2]}')
                print(f'- Peso: {pokemon[3]}')
                print(f'- Tipo: {pokemon[4]}')
                print('\n-----------------------------------')

def main():
    try:
        poke_id = int(input('\nIngrese el ID del Pokemon: '))
        json_data = create_http_request(poke_id)

        pokemon = create_pokemon_object(json_data)
        save_to_database(pokemon)
        list_pokemons()

        print(f'\n- ¡Datos del Pokemon "{pokemon.name}" guardados en la DB!\n')

    except requests.exceptions.RequestException as re:
        print(f'\n- Error en la solicitud HTTP: {re}\n')

    except Exception as e:
        print(f'\n- Error: {e}\n')

if __name__ == '__main__':
    main()
