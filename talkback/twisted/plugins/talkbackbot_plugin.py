from ConfigParser import ConfigParser

from twisted.application.service import IServiceMaker, Service
from twisted.internet.endpoints import clientFromString
from twisted.plugin import IPlugin
from twisted.python import usage, log
from zope.interface import implementer

from talkback.bot import TalkBackBotFactory
from talkback.quote_picker import QuotePicker

class Options(usage.Options):
    optParameters = [
        ['config', 'c', 'settings.ini', 'Configuration file.'],
    ]

class TalkBackBotService(Service):

    def __init__(self, endpoint, channel, nickname, realname, quotesFilename,
                 triggers):
        self._endpoint = endpoint
        self._channel = channel
        self._nickname = nickname
        self._realname = realname
        self._quotesFilename = quotesFilename
        self._triggers = triggers

    def startService(self):
        """Construct a client & connect to server."""

    def stopService(self):
        """Disconnect."""

@implementer(IServiceMaker, IPlugin)
class BotServiceMaker(object):
    tapname = "twsrs"
    description = "IRC bot that provides quotations from notable women"
    options = Options

    def makeService(self, options):
        """Construct the talkbackbot service."""
        config = ConfigParser()
        config.read([options['config']])
        triggers = [
            trigger.strip()
            for trigger
            in config.get('talkback', 'triggers').split('\n')
            if trigger.strip()
        ]

        return TalkBackBotService(
            endpoint = config.get('irc', 'endpoint'),
            channel = config.get('irc', 'channel'),
            nickname = config.get('irc', 'nickname'),
            realname = config.get('irc', 'realname'),
            quotesFilename = config.get('talkback', 'quotesFilename'),
            triggers = triggers
        )


serviceMaker = BotServiceMaker()
