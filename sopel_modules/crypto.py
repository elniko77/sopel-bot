"""sopel-btc

Plugin para sopel, obtiene cotización del bitcoin desde varias apis.
"""
from sopel import module
import requests
import json
import re

@module.commands('crypto')
def crypto(bot, trigger):

    api_bitso = 'https://api.bitso.com/v3/ticker/?book='
    
    monedas = { 'Ripple': 'xrp_usd', 'Ethereum' : 'eth_usd', 'Dai(ars)' : 'dai_ars' }

    mensaje = ""

    for token in monedas:
        apiurl = api_bitso + monedas[token]
        try:
            r = requests.get(apiurl)
        except:
            raise Exception("Error obteniendo cotización... ‾_(ツ)_/‾")
    
        data = r.json()
        
  
        if r.status_code != 200:
            raise Exception('Error: {}'.format(data['message']))
        else:
            if (data['success']):
                mensaje = mensaje + f"[{token}] {data['payload']['bid']} "
    
    bot.say(mensaje)