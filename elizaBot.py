import json
from random import choice
from lxml import objectify
from eliza import Eliza
from errbot import botcmd, BotPlugin, PY2

if PY2:
    from urllib2 import urlopen, quote
else:
    from urllib.request import urlopen, quote

class ElizaBot(BotPlugin):
    eliza_daemon = Eliza()

    @botcmd
    def eliza(self, _, args):
        """ El'cheapo shrink for you """
        args = args.strip()
        return self.eliza_daemon.respond(args)

    @botcmd
    def askus(self, _, __):
        """ Give us a fun topic to talk about
            thx to http://chatoms.com/
        """
        content = urlopen('http://chatoms.com/chatom.json?Normal=1&Fun=2&Philosophy=3&Out+There=4&Love=5&Personal=7').read()
        return json.loads(content.decode())['text']

    @botcmd
    def complete(self, _, args):
        """ Complete the given sentence
            thx to the awesome google completion
        """
        args = args.strip()
        if not args:
            return 'Complete what ?'

        content = urlopen('http://google.com/complete/search?q=%s&output=toolbar' % quote(args)).read()
        xml = objectify.fromstring(content)
        possibilities = xml.xpath("//toplevel/CompleteSuggestion/suggestion/@data")
        if possibilities:
            return choice(possibilities)
        return 'Hmmm... no answer for that'