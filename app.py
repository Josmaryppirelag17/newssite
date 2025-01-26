from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# Ingresa tu clave de API aquí
API_KEY = 'dae35e73de4b42a39c2419da725c8d28'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'GET':
        return redirect('/')  # Redirige a la página principal si se accede con GET

    tema = request.form['tema']
    url = f'https://newsapi.org/v2/everything?q={tema}&apiKey={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        return render_template('results.html', articles=articles, tema=tema)
    else:
        error_message = f"Error en la solicitud: {response.status_code}"
        return render_template('results.html', error=error_message, tema=tema)

if __name__ == '__main__':
    app.run(debug=True)
