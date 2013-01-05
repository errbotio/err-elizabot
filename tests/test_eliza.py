# coding=utf-8
from errbot.backends.test import FullStackTest, pushMessage, popMessage


class TestCommands(FullStackTest):
    @classmethod
    def setUpClass(cls, extra=None):
        super(TestCommands, cls).setUpClass(__file__)

    def test_eliza(self):
        pushMessage('!eliza Hello')
        self.assertRegex(popMessage(), r"Hi|Hello")

    def test_askus(self):
        self.assertCommandFound('!askus')

    def test_complete(self):
        self.assertCommand('!complete paris is', 'paris is')