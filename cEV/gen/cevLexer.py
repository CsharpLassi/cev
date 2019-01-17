# Generated from /home/lassi/Dokumente/develop/cEV/cEV/cev.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("!\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\13\n\2\r\2\16\2")
        buf.write("\f\3\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2\5\2\26\n\2\3\3")
        buf.write("\3\3\3\3\3\3\5\3\34\n\3\3\4\3\4\3\4\3\4\2\2\5\3\3\5\4")
        buf.write("\7\5\3\2\4\3\2\62;\3\2\60\60\2$\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\3\n\3\2\2\2\5\33\3\2\2\2\7\35\3\2\2\2\t")
        buf.write("\13\t\2\2\2\n\t\3\2\2\2\13\f\3\2\2\2\f\n\3\2\2\2\f\r\3")
        buf.write("\2\2\2\r\25\3\2\2\2\16\22\t\3\2\2\17\21\t\2\2\2\20\17")
        buf.write("\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23")
        buf.write("\26\3\2\2\2\24\22\3\2\2\2\25\16\3\2\2\2\25\26\3\2\2\2")
        buf.write("\26\4\3\2\2\2\27\30\7Q\2\2\30\31\7j\2\2\31\34\7o\2\2\32")
        buf.write("\34\7T\2\2\33\27\3\2\2\2\33\32\3\2\2\2\34\6\3\2\2\2\35")
        buf.write("\36\7\"\2\2\36\37\3\2\2\2\37 \b\4\2\2 \b\3\2\2\2\7\2\f")
        buf.write("\22\25\33\3\b\2\2")
        return buf.getvalue()


class cevLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER = 1
    UNIT_RESISTOR = 2
    WHITESPACE = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "' '" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "UNIT_RESISTOR", "WHITESPACE" ]

    ruleNames = [ "NUMBER", "UNIT_RESISTOR", "WHITESPACE" ]

    grammarFileName = "cev.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


