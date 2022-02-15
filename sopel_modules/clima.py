from sopel import module
from sopel.config.types import StaticSection, ValidatedAttribute
import requests
import re

@module.commands('clima')
def clima(bot, trigger):
    city = trigger.group(2)

    trigger = re.sub('(<.*?>) ?', '', trigger)
    trigger = re.sub(r'\..\S*(\s)?', '', trigger)

    if (not trigger):
        bot.say('Uso: clima <ciudad>')
        return
    else:
        city = trigger

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

    #apiurl = apiurl + '&q=' + city + ',ar' 
    apiurlarg = apiurl + '&q=' + city + ',ar'
    apiurl = apiurl + '&q=' + city

    # Primero se intenta con país Argentina, si no lo encuentra se prueba
    try:
        r = requests.get(apiurlarg)
    except:
        raise Exception("Error obteniendo clima... ‾_(ツ)_/‾")

    data = r.json()
    if r.status_code != 200:
        #Ahora se prueba sin el codigo de país
        try:
            r = requests.get(apiurl)
        except:
            raise Exception("Error obteniendo clima... ‾_(ツ)_/‾")
        data = r.json()
        if r.status_code != 200:
            raise Exception('Error: {}'.format(data['message']))
        else:
            clima = f"{data['name']}, {data['sys']['country']}: {data['main']['temp']}˚C - {iconos[data['weather'][0]['icon']]}  - min: {data['main']['temp_min']}˚C, max: {data['main']['temp_min']}˚C - humedad: {data['main']['humidity']}% - ST: {data['main']['feels_like']}˚C - Presión: {data['main']['pressure']}hPa."
            bot.say(clima)
    else:
        clima = f"{data['name']}, {data['sys']['country']}: {data['main']['temp']}˚C - {iconos[data['weather'][0]['icon']]}  - min: {data['main']['temp_min']}˚C, max: {data['main']['temp_min']}˚C - humedad: {data['main']['humidity']}%. - ST: {data['main']['feels_like']}˚C - Presión: {data['main']['pressure']}hPa."
        bot.say(clima)
