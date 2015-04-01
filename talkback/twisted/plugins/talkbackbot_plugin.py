from ConfigParser import ConfigParser

from twisted.application.service import IServiceMaker, Service
from twisted.internet.endpoints import clientFromString
from twisted.plugin import IPlugin
from twisted.python import usage, log
from zope.interface import implementer

from talkback.bot import TalkBackBotFactory
from talkback.quote_picker import QuotePicker

class Options(usage.Options):

class TalkBackBotService(Service):

    def __init__(self, endpoint, channel, nickname, realname, quotesFilename, triggers):

    def startService(self):
        """Construct a client & connect to server."""

    def stopService(self):
        """Disconnect."""

class BotServiceMaker(object):
    tapname = "twsrs"
    description = "IRC bot that provides quotations from notable women"
    options = Options

    def makeService(self, options):
        """Construct the talkbackbot service."""


serviceMaker = BotServiceMaker()
