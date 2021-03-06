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
        '01d' : 'âï¸',
        '01n' : 'ð',
        '02d' : 'ð¥',
        '02n' : 'ð¥',
        '03d' : 'âï¸',
        '03n' : 'âï¸',
        '04d' : 'âï¸',
        '04n' : 'âï¸',
        '09d' : 'ð¦',
        '09n' : 'ð¦',
        '10d' : 'ð§',
        '10n' : 'ð§',
        '11d' : 'â',
        '11n' : 'â',
        '13d' : 'ð¨',
        '13n' : 'ð¨',
        '50d' : 'ð«',
        '50n' : 'ð«'
    }

    #apiurl = apiurl + '&q=' + city + ',ar' 
    apiurlarg = apiurl + '&q=' + city + ',ar'
    apiurl = apiurl + '&q=' + city

    # Primero se intenta con paÃ­s Argentina, si no lo encuentra se prueba
    try:
        r = requests.get(apiurlarg)
    except:
        raise Exception("Error obteniendo clima... â¾_(ã)_/â¾")

    data = r.json()
    if r.status_code != 200:
        #Ahora se prueba sin el codigo de paÃ­s
        try:
            r = requests.get(apiurl)
        except:
            raise Exception("Error obteniendo clima... â¾_(ã)_/â¾")
        data = r.json()
        if r.status_code != 200:
            raise Exception('Error: {}'.format(data['message']))
        else:
            clima = f"{data['name']}, {data['sys']['country']}: {data['main']['temp']}ËC - {iconos[data['weather'][0]['icon']]}  - min: {data['main']['temp_min']}ËC, max: {data['main']['temp_min']}ËC - humedad: {data['main']['humidity']}% - ST: {data['main']['feels_like']}ËC - PresiÃ³n: {data['main']['pressure']}hPa."
            bot.say(clima)
    else:
        clima = f"{data['name']}, {data['sys']['country']}: {data['main']['temp']}ËC - {iconos[data['weather'][0]['icon']]}  - min: {data['main']['temp_min']}ËC, max: {data['main']['temp_min']}ËC - humedad: {data['main']['humidity']}%. - ST: {data['main']['feels_like']}ËC - PresiÃ³n: {data['main']['pressure']}hPa."
        bot.say(clima)
