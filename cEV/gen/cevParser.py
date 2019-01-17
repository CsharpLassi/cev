# Generated from /home/lassi/Dokumente/develop/cEV/cEV/cev.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\f\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\3\3\2\2\4\2\4\2")
        buf.write("\2\2\t\2\6\3\2\2\2\4\b\3\2\2\2\6\7\5\4\3\2\7\3\3\2\2\2")
        buf.write("\b\t\7\3\2\2\t\n\7\4\2\2\n\5\3\2\2\2\2")
        return buf.getvalue()


class cevParser ( Parser ):

    grammarFileName = "cev.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "UNIT_RESISTOR", "WHITESPACE" ]

    RULE_stmt = 0
    RULE_resistor = 1

    ruleNames =  [ "stmt", "resistor" ]

    EOF = Token.EOF
    NUMBER=1
    UNIT_RESISTOR=2
    WHITESPACE=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def resistor(self):
            return self.getTypedRuleContext(cevParser.ResistorContext,0)


        def getRuleIndex(self):
            return cevParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = cevParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.resistor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResistorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None # Token

        def UNIT_RESISTOR(self):
            return self.getToken(cevParser.UNIT_RESISTOR, 0)

        def NUMBER(self):
            return self.getToken(cevParser.NUMBER, 0)

        def getRuleIndex(self):
            return cevParser.RULE_resistor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResistor" ):
                listener.enterResistor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResistor" ):
                listener.exitResistor(self)




    def resistor(self):

        localctx = cevParser.ResistorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_resistor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            localctx.value = self.match(cevParser.NUMBER)
            self.state = 7
            self.match(cevParser.UNIT_RESISTOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





