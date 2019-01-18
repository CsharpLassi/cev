# Generated from /home/lassi/Dokumente/develop/cEV/cEV/cev.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("J\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\6\n\60\n\n\r\n\16\n\61\3\n\3")
        buf.write("\n\7\n\66\n\n\f\n\16\n9\13\n\5\n;\n\n\3\13\3\13\3\13\3")
        buf.write("\13\5\13A\n\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\2\2")
        buf.write("\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\3\2\4\3\2\62;\3\2\60\60\2M\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2")
        buf.write("\2\5\37\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r(\3")
        buf.write("\2\2\2\17*\3\2\2\2\21,\3\2\2\2\23/\3\2\2\2\25@\3\2\2\2")
        buf.write("\27B\3\2\2\2\31D\3\2\2\2\33F\3\2\2\2\35\36\7W\2\2\36\4")
        buf.write("\3\2\2\2\37 \7*\2\2 \6\3\2\2\2!\"\7+\2\2\"\b\3\2\2\2#")
        buf.write("$\7-\2\2$\n\3\2\2\2%&\7~\2\2&\'\7~\2\2\'\f\3\2\2\2()\7")
        buf.write(".\2\2)\16\3\2\2\2*+\7K\2\2+\20\3\2\2\2,-\7?\2\2-\22\3")
        buf.write("\2\2\2.\60\t\2\2\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2")
        buf.write("\61\62\3\2\2\2\62:\3\2\2\2\63\67\t\3\2\2\64\66\t\2\2\2")
        buf.write("\65\64\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28")
        buf.write(";\3\2\2\29\67\3\2\2\2:\63\3\2\2\2:;\3\2\2\2;\24\3\2\2")
        buf.write("\2<=\7Q\2\2=>\7j\2\2>A\7o\2\2?A\7T\2\2@<\3\2\2\2@?\3\2")
        buf.write("\2\2A\26\3\2\2\2BC\7X\2\2C\30\3\2\2\2DE\7C\2\2E\32\3\2")
        buf.write("\2\2FG\7\"\2\2GH\3\2\2\2HI\b\16\2\2I\34\3\2\2\2\7\2\61")
        buf.write("\67:@\3\b\2\2")
        return buf.getvalue()


class cevLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    NUMBER = 9
    UNIT_RESISTOR = 10
    UNIT_VOLTAGE = 11
    UNIT_CURRENT = 12
    WHITESPACE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'U'", "'('", "')'", "'+'", "'||'", "','", "'I'", "'='", "'V'", 
            "'A'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "UNIT_RESISTOR", "UNIT_VOLTAGE", "UNIT_CURRENT", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "NUMBER", "UNIT_RESISTOR", "UNIT_VOLTAGE", "UNIT_CURRENT", 
                  "WHITESPACE" ]

    grammarFileName = "cev.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


