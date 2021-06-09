from sopel import module
from sopel.config.types import StaticSection, ValidatedAttribute
import requests

@module.commands('feriado')
def feriado(bot, trigger):
    year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())

    meses  = { 1 : 'Enero', 2 : 'Febrero', 3 : 'Marzo', 4 : 'Abril', 5: 'Mayo', 6 : 'Junio', 7: 'Julio', 8 : 'Agosto', 9: 'Septiembre', 10 : 'Octubre', 11 : 'Noviembre', 12 : 'Diciembre' }

    api_url = 'http://nolaborables.com.ar/api/v2/feriados/'
    api_request = api_url + str(year) + '?formato=mensual'

    try:
        r = requests.get(api_request)
    except:
        raise Exception("Error obteniendo feriados... ‾_(ツ)_/‾")

    #month = 10  
    #day = 13

    data = r.json()
    if r.status_code != 200:
        raise Exception('Error: {}'.format(data['message']))
    else:
        i = month - 1
        while i < 12:
            for feriado in data[i]:
                if int(feriado) == day:
                    bot.say("Hoy es feriado!!")
                    return
                else: 
                    if int(feriado) > day:
                        fecha_hoy = date(int(year), int(month), int(day))
                        fecha_feriado = date(int(year), i+1, int(feriado))
                        dias = fecha_feriado - fecha_hoy
                        mensaje = f"El próximo feriado es el {feriado} de {meses[i+1]}, {data[i][feriado]['motivo']}. Faltan {dias.days} días."
                        bot.say(mensaje)
                        return 
            i = i + 1
        bot.say("No hay mas feriados en el año")
