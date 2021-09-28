"""sopel-gold

Plugin para sopel, obtiene cotización del oro.
"""
from sopel import module
import requests
import json
import re

@module.commands('gold')
def gold(bot, trigger):

    api_coingecko = 'https://api.coingecko.com/api/v3/coins/tether-gold?localization=false&community_data=false&developer_data=false&sparkline=false'
    mensaje = ""

    try:
        r = requests.get(api_coingecko)
    except:
        raise Exception("Error obteniendo cotización... ‾_(ツ)_/‾")

    data = r.json()

    if r.status_code != 200:
        raise Exception('Error: {}'.format(data['message']))
    else:
        mensaje = f"[Gold - Tether-gold (xaut)] {data['market_data']['current_price']['usd']}"


    bot.say(mensaje)
