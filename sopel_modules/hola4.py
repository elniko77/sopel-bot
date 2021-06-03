from sopel import module

@module.commands('hola4')
def hola4(bot, trigger):
    bot.say('Hello, world! 4')
