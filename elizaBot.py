import json
from random import choice
from lxml import objectify
from eliza import Eliza
from urllib2 import urlopen,quote

# Backward compatibility
from errbot.version import VERSION
from errbot.utils import version2array
if version2array(VERSION) >= [1,6,0]:
    from errbot import botcmd, BotPlugin
else:
    from errbot.botplugin import BotPlugin
    from errbot.jabberbot import botcmd



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
            thx to http://chatoms.com/
        """
        content = urlopen('http://chatoms.com/chatom.json?Normal=1&Fun=2&Philosophy=3&Out+There=4&Love=5&Personal=7').read()
        return json.loads(content)['text']

    @botcmd
    def complete(self, mess, args):
        """ Complete the given sentence
            thx to the awesome google completion
        """
        args = args.strip()
        if not args:
            return 'Complete what ?'

        content = urlopen('http://google.com/complete/search?q=%s&output=toolbar'%quote(args)).read()
        xml = objectify.fromstring(content)
        possibilities = xml.xpath("//toplevel/CompleteSuggestion/suggestion/@data")
        if possibilities:
            return choice(possibilities)
        return 'Hmmm... no answer for that'

