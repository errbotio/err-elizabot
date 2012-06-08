from errbot.botplugin import BotPlugin
from eliza import Eliza
from errbot.jabberbot import botcmd

__author__ = 'gbin'

class ElizaBot(BotPlugin):
    eliza_daemon = Eliza()
    @botcmd
    def eliza(self, mess, args):
        """ El'cheapo shrink for you """
        args = args.strip()
        return self.eliza_daemon.respond(args)

