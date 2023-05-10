import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = 'baa6dddd74974e3180cff0f4d73068ac'
    url = f'https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}'

    response = requests.get(url).json()

    if response['data'] == []:
        return render_template('error.html')

    weather = {
        'city': response['data'][0]['city_name'],
        'temperature': response['data'][0]['temp'],
        'description': response['data'][0]['weather']['description'].capitalize(),
        'icon': f'https://www.weatherbit.io/static/img/icons/{response["data"][0]["weather"]["icon"]}.png'
    }

    return render_template('weather.html', weather=weather)
if __name__ == '__main__':
    app.run(debug=True)
