from flask import Flask, render_template
import json
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/films')
def buscaPeliculas():
    url = 'http://www.omdbapi.com/?t=superman&apikey=1eee63f9'
    response = requests.get(url)
  
    if response.status_code == 200:
        content = response.content
        file = open('templates/resultados.html', 'wb')
        file.write(content)
        file.close()

    return render_template('films.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    