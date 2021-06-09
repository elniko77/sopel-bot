"""sopel-dolar

Plugin para sopel para obtener cotización del dólar
"""

from sopel import module
import requests
import json

@module.commands('dolar')
def dolar(bot, trigger):

    cuantos = trigger.group(2)

    if not cuantos:
        cuantos = float(1)
    else:
        cuantos = float(cuantos)
          

    api_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
    tipodolar = ["Dolar Oficial", "Dolar Blue", "Dolar Bolsa", "Dolar Contado con Liqui"]
    
    try:
        r = requests.get(api_url)
    except:
        raise Exception("Error obteniendo cotización del dolar... ‾_(ツ)_/‾")
    
    data = r.json()
    mensaje = ""
    if r.status_code != 200:
        raise Exception('Error: {}'.format(data['message']))
    else:
        for cotizacion in data:
            if (cotizacion['casa']['nombre'] in tipodolar):
                compra = float(cotizacion['casa']['compra'].replace(',', '.')) * cuantos
                venta = float(cotizacion['casa']['venta'].replace(',', '.')) * cuantos

                mensaje = mensaje + f"[{cotizacion['casa']['nombre']}] {compra:.2f} - {venta:.2f} ::  " 
                
            if(cotizacion['casa']['nombre'] == 'Dolar Oficial'):
                    #solidario = venta * 1.65 * $howmuch if $type eq 'Dolar Oficial';
                    solidario = float(venta) * 1.65
        
        mensaje = mensaje + f"[Dolar Solidario ahorro] $ {solidario:.2f}"
        bot.say(mensaje)
