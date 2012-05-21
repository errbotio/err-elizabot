from botplugin import BotPlugin
import eliza
from jabberbot import botcmd
from utils import get_jid_from_message

__author__ = 'gbin'

class ElizaBot(BotPlugin):
    eliza_daemon = eliza()
    @botcmd
    def eliza(self, mess, args):
        """ El'cheapo shrink for you """
        args = args.strip()
        return self.eliza_daemon.respond(args)

    def callback_message(self, conn, mess):
        pass
