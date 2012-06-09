import json
from errbot.botplugin import BotPlugin
from eliza import Eliza
from errbot.jabberbot import botcmd
from urllib2 import urlopen

__author__ = 'gbin'

class ElizaBot(BotPlugin):
    eliza_daemon = Eliza()
    @botcmd
    def eliza(self, mess, args):
        """ El'cheapo shrink for you """
        args = args.strip()
        return self.eliza_daemon.respond(args)

    @botcmd
    def askus(self, mess, args):
        """ Give us a fun topic to talk about
        """
        content = urlopen('http://chatoms.com/chatom.json?Normal=1&Fun=2&Philosophy=3&Out+There=4&Love=5&Personal=7').read()
        return json.loads(content)['text']


