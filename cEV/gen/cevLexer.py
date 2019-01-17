# Generated from /home/lassi/Dokumente/develop/cEV/cEV/cev.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("*\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\4\6\4\24\n\4\r\4\16\4\25\3\4\3\4\7\4\32")
        buf.write("\n\4\f\4\16\4\35\13\4\5\4\37\n\4\3\5\3\5\3\5\3\5\5\5%")
        buf.write("\n\5\3\6\3\6\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13\7\3\2\4")
        buf.write("\3\2\62;\3\2\60\60\2-\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\17\3\2\2\2")
        buf.write("\7\23\3\2\2\2\t$\3\2\2\2\13&\3\2\2\2\r\16\7-\2\2\16\4")
        buf.write("\3\2\2\2\17\20\7~\2\2\20\21\7~\2\2\21\6\3\2\2\2\22\24")
        buf.write("\t\2\2\2\23\22\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2\2\25")
        buf.write("\26\3\2\2\2\26\36\3\2\2\2\27\33\t\3\2\2\30\32\t\2\2\2")
        buf.write("\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2")
        buf.write("\2\34\37\3\2\2\2\35\33\3\2\2\2\36\27\3\2\2\2\36\37\3\2")
        buf.write("\2\2\37\b\3\2\2\2 !\7Q\2\2!\"\7j\2\2\"%\7o\2\2#%\7T\2")
        buf.write("\2$ \3\2\2\2$#\3\2\2\2%\n\3\2\2\2&\'\7\"\2\2\'(\3\2\2")
        buf.write("\2()\b\6\2\2)\f\3\2\2\2\7\2\25\33\36$\3\b\2\2")
        return buf.getvalue()


class cevLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    NUMBER = 3
    UNIT_RESISTOR = 4
    WHITESPACE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'||'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "UNIT_RESISTOR", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "NUMBER", "UNIT_RESISTOR", "WHITESPACE" ]

    grammarFileName = "cev.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


