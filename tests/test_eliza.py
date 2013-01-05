# coding=utf-8
from errbot.backends.test import FullStackTest, pushMessage, popMessage
from errbot import PY3


class TestCommands(FullStackTest):
    @classmethod
    def setUpClass(cls, extra=None):
        super(TestCommands, cls).setUpClass(__file__)

    def test_eliza(self):
        pushMessage('!eliza Hello')
        ref = self.assertRegex if PY3 else self.assertRegexpMatches
        ref(popMessage(), r"Hi|Hello")

    def test_askus(self):
        self.assertCommandFound('!askus')

    def test_complete(self):
        self.assertCommand('!complete paris is', 'paris is')