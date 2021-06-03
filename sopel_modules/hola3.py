from sopel import module

@module.commands('hola3')
def hola3(bot, trigger):
    bot.say('Hello, world! 3')
