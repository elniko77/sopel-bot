# sopel-bot

Plugins para bot-sopel, usados en canales de #sysarmy en libera.

Para correr el bot, configurar sopel_config/default.cfg con los canales y el servidor irc al que conectarse. (Copiar el default.cfg.example) y levantarlo en docker:

```docker-compose up```

Para desarrollar los plugins localmente, hay un docker-compose que levanta un weechat, y un server de irc. Correrlo de esta forma:

```docker-compose -f docker-compose-test.yaml up -d```

Y para interactuar con weechat:

```docker attach weechat2```

