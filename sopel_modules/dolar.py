"""sopel-dolar

Plugin para sopel para obtener cotización del dólar
"""

from sopel import module
import requests
import json

@module.commands('dolar')
def dolar(bot, trigger):
#    bot.say('Hello, world! 4')
    data = requests.get('http://api.bluelytics.com.ar/v2/latest')

    if data.status_code == 200:
        jdata = data.json()
            
        oficial = jdata["oficial"]["value_avg"]
        blue = jdata["blue"]["value_avg"]
        dolarprice = 'Oficial: ' + str(oficial) + ' / Blue: ' + str(blue)
        bot.say(dolarprice)
    else:
        return 'Problemas con la api'
