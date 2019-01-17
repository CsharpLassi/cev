# Generated from /home/lassi/Dokumente/develop/cEV/cEV/cev.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("%\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\6\3")
        buf.write("\17\n\3\r\3\16\3\20\3\3\3\3\7\3\25\n\3\f\3\16\3\30\13")
        buf.write("\3\5\3\32\n\3\3\4\3\4\3\4\3\4\5\4 \n\4\3\5\3\5\3\5\3\5")
        buf.write("\2\2\6\3\3\5\4\7\5\t\6\3\2\4\3\2\62;\3\2\60\60\2(\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\13\3\2")
        buf.write("\2\2\5\16\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13\f\7-\2\2")
        buf.write("\f\4\3\2\2\2\r\17\t\2\2\2\16\r\3\2\2\2\17\20\3\2\2\2\20")
        buf.write("\16\3\2\2\2\20\21\3\2\2\2\21\31\3\2\2\2\22\26\t\3\2\2")
        buf.write("\23\25\t\2\2\2\24\23\3\2\2\2\25\30\3\2\2\2\26\24\3\2\2")
        buf.write("\2\26\27\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\31\22\3\2")
        buf.write("\2\2\31\32\3\2\2\2\32\6\3\2\2\2\33\34\7Q\2\2\34\35\7j")
        buf.write("\2\2\35 \7o\2\2\36 \7T\2\2\37\33\3\2\2\2\37\36\3\2\2\2")
        buf.write(" \b\3\2\2\2!\"\7\"\2\2\"#\3\2\2\2#$\b\5\2\2$\n\3\2\2\2")
        buf.write("\7\2\20\26\31\37\3\b\2\2")
        return buf.getvalue()


class cevLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    NUMBER = 2
    UNIT_RESISTOR = 3
    WHITESPACE = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "UNIT_RESISTOR", "WHITESPACE" ]

    ruleNames = [ "T__0", "NUMBER", "UNIT_RESISTOR", "WHITESPACE" ]

    grammarFileName = "cev.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


