from sopel import module
from sopel.config.types import StaticSection, ValidatedAttribute
import requests

@module.commands('clima')
def clima(bot, trigger):
    city = trigger.group(2)

    if not city:
        bot.say('Uso: clima <ciudad>')
        return

#    bot.say(city)

    api_key = bot.config.clima.api_key
    apiurl = 'http://api.openweathermap.org/data/2.5/weather?units=metric&appid=' + api_key

    iconos = {
        '01d' : '☀️',
        '01n' : '🌙',
        '02d' : '🌥',
        '02n' : '🌥',
        '03d' : '☁️',
        '03n' : '☁️',
        '04d' : '☁️',
        '04n' : '☁️',
        '09d' : '🌦',
        '09n' : '🌦',
        '10d' : '🌧',
        '10n' : '🌧',
        '11d' : '⛈',
        '11n' : '⛈',
        '13d' : '🌨',
        '13n' : '🌨',
        '50d' : '🌫',
        '50n' : '🌫'
    }

    apiurl = apiurl + '&q=' + city + ',ar' 

    try:
        r = requests.get(apiurl)
    except:
        raise Exception("Error obteniendo clima... ‾_(ツ)_/‾")

    
    data = r.json()
    if r.status_code != 200:
        raise Exception('Error: {}'.format(data['message']))
    else:
        #f"{data['name']}, {data['sys']['country']}: {data['main']['temp']} - {data['weather'][0]['icon']} - min: {data['main']['temp_min']}, max: {data['main']['temp_min']} - humedad: {data['main']['humidity']} ."
        clima = f"{data['name']}, {data['sys']['country']}: {data['main']['temp']}˚C - {iconos[data['weather'][0]['icon']]}  - min: {data['main']['temp_min']}˚C, max: {data['main']['temp_min']}˚C - humedad: {data['main']['humidity']}%."
        bot.say(clima)
