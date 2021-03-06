import requests
import configparser
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/results2', methods=['GET', 'POST'])
def weather_dashboard2():
    # zip_code = request.form['zipCode']
    # print('zc       ', zip_code)
    return "zippo " 



@app.route('/results', methods=['GET', 'POST'])
def render_results():
    zip_code = request.form['zipCode']
    print('zc       ', zip_code)
    return "zippo " + zip_code


if __name__ == '__main__':
    app.run()


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather_results(zip_code, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}".format(zip_code, api_key)
    print('asda', api_url)
    r = requests.get(api_url)
    return r.json()


# print('penguin', get_weather_results("95129", get_api_key()))