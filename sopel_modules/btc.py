"""sopel-btc

Plugin para sopel, obtiene cotización del bitcoin desde varias apis.
"""
from sopel import module
import requests
import json

@module.commands('btc')
def btc(bot, trigger):

    #ordenar y poner en funciones    
    api_bitso = 'https://api.bitso.com/v3/ticker/?book=btc_usd'
    
    try:
        r = requests.get(api_bitso)
    except:
        raise Exception("Error obteniendo cotización del btc... ‾_(ツ)_/‾")
    
    data = r.json()
    mensaje = ""
    
    
    if r.status_code != 200:
        raise Exception('Error: {}'.format(data['message']))
    else:
        if (data['success']):
            mensaje = f"[Bitso] {data['payload']['bid']}"     


    api_coinbase = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
    
    try:
        r = requests.get(api_coinbase)
    except:
        raise Exception("Error obteniendo cotización del btc... ‾_(ツ)_/‾")
    
    data = r.json()
    
    if r.status_code != 200:
        raise Exception('Error: {}'.format(data['message']))
    else:
        mensaje = mensaje + f" :: [Coinbase] {data['data']['amount']}"     
    
    bot.say(mensaje)
