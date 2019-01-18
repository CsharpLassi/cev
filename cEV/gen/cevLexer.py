# Generated from /home/lassi/Dokumente/develop/cEV/cEV/cev.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write(".\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\4\6\4\26\n\4\r\4\16\4\27\3\4\3")
        buf.write("\4\7\4\34\n\4\f\4\16\4\37\13\4\5\4!\n\4\3\5\3\5\3\5\3")
        buf.write("\5\5\5\'\n\5\3\6\3\6\3\7\3\7\3\7\3\7\2\2\b\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\3\2\4\3\2\62;\3\2\60\60\2\61\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\3\17\3\2\2\2\5\21\3\2\2\2\7\25\3\2\2\2\t&\3\2")
        buf.write("\2\2\13(\3\2\2\2\r*\3\2\2\2\17\20\7-\2\2\20\4\3\2\2\2")
        buf.write("\21\22\7~\2\2\22\23\7~\2\2\23\6\3\2\2\2\24\26\t\2\2\2")
        buf.write("\25\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2")
        buf.write("\2\30 \3\2\2\2\31\35\t\3\2\2\32\34\t\2\2\2\33\32\3\2\2")
        buf.write("\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36!\3\2\2")
        buf.write("\2\37\35\3\2\2\2 \31\3\2\2\2 !\3\2\2\2!\b\3\2\2\2\"#\7")
        buf.write("Q\2\2#$\7j\2\2$\'\7o\2\2%\'\7T\2\2&\"\3\2\2\2&%\3\2\2")
        buf.write("\2\'\n\3\2\2\2()\7X\2\2)\f\3\2\2\2*+\7\"\2\2+,\3\2\2\2")
        buf.write(",-\b\7\2\2-\16\3\2\2\2\7\2\27\35 &\3\b\2\2")
        return buf.getvalue()


class cevLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    NUMBER = 3
    UNIT_RESISTOR = 4
    UNIT_VOLTAGE = 5
    WHITESPACE = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'||'", "'V'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "UNIT_RESISTOR", "UNIT_VOLTAGE", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "NUMBER", "UNIT_RESISTOR", "UNIT_VOLTAGE", 
                  "WHITESPACE" ]

    grammarFileName = "cev.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


