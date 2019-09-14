from flask import Flask, render_template, request
import json
import requests
import configparser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/films')
def buscaPeliculas():
    
    # obtenemos el valor a buscar
    buscar = request.args.get('buscar')

    # formamos la url de búsqueda con la variable a buscar
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config['omdbapi.com']['API_KEY']
    url = config['omdbapi.com']['ALL_MOVIES']
    url = url.format(api_key, buscar) #la variable url machaca la de la linea de anterior

    # Obtenemos la respuesta de la api con la url formada
    json_api_response = requests.get(url).json()

    # Sacamos las películas del objeto
    film_results = json_api_response["Search"]

    # Renderizamos la vista con los resultados de la búsqueda
    return render_template('films.html', results = film_results)

if __name__ == '__main__':
    app.run(debug=True)
    
    