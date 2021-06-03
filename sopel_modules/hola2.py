from sopel import module

@module.commands('hola2')
def hola2(bot, trigger):
    bot.say('Hello, world! 2')
