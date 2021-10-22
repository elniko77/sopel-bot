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
    api_coingecko = 'https://api.coingecko.com/api/v3/coins/cardano?localization=false&community_data=false&developer_data=false&sparkline=false'
    api_alpha =  'https://api.coingecko.com/api/v3/coins/alpha-finance?localization=false&community_data=false&developer_data=false&sparkline=false'

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

    try:
        r = requests.get(api_coingecko)
    except:
        raise Exception("Error obteniendo cotización... ‾_(ツ)_/‾")

    data = r.json()

    if r.status_code != 200:
        raise Exception('Error: {}'.format(data['message']))
    else:
        mensaje = mensaje + f"[Cardano] {data['market_data']['current_price']['usd']} "


    try:
        r = requests.get(api_alpha)
    except:
        raise Exception("Error obteniendo cotización... ‾_(ツ)_/‾")

    data = r.json()

    if r.status_code != 200:
        raise Exception('Error: {}'.format(data['message']))
    else:
        mensaje = mensaje + f"[Alpha] {data['market_data']['current_price']['usd']}"


    api_coinbase = 'https://api.coinbase.com/v2/prices/spot?currency=USD'

    try:
        r = requests.get(api_coinbase)
    except:
        raise Exception("Error obteniendo cotización del btc... ‾_(ツ)_/‾")
    data = r.json()

    if r.status_code != 200:
        raise Exception('Error: {}'.format(data['message']))
    else:
        mensaje = mensaje + f" [Btc] {float(data['data']['amount']):.2f}"


    bot.say(mensaje)
