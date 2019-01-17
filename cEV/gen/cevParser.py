# Generated from /home/lassi/Dokumente/develop/cEV/cEV/cev.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\31\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\7\3\21\n\3\f\3\16\3\24\13\3\3\4\3\4\3\4\3\4\2\3")
        buf.write("\4\5\2\4\6\2\2\2\26\2\b\3\2\2\2\4\n\3\2\2\2\6\25\3\2\2")
        buf.write("\2\b\t\5\4\3\2\t\3\3\2\2\2\n\13\b\3\1\2\13\f\5\6\4\2\f")
        buf.write("\22\3\2\2\2\r\16\f\4\2\2\16\17\7\3\2\2\17\21\5\4\3\5\20")
        buf.write("\r\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23")
        buf.write("\5\3\2\2\2\24\22\3\2\2\2\25\26\7\4\2\2\26\27\7\5\2\2\27")
        buf.write("\7\3\2\2\2\3\22")
        return buf.getvalue()


class cevParser ( Parser ):

    grammarFileName = "cev.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "<INVALID>", "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NUMBER", "UNIT_RESISTOR", 
                      "WHITESPACE" ]

    RULE_stmt = 0
    RULE_connection = 1
    RULE_resistor = 2

    ruleNames =  [ "stmt", "connection", "resistor" ]

    EOF = Token.EOF
    T__0=1
    NUMBER=2
    UNIT_RESISTOR=3
    WHITESPACE=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def connection(self):
            return self.getTypedRuleContext(cevParser.ConnectionContext,0)


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
            self.state = 6
            self.connection(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConnectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cevParser.RULE_connection

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ElementContext(ConnectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cevParser.ConnectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def resistor(self):
            return self.getTypedRuleContext(cevParser.ResistorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)


    class Series_connectionContext(ConnectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cevParser.ConnectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def connection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cevParser.ConnectionContext)
            else:
                return self.getTypedRuleContext(cevParser.ConnectionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeries_connection" ):
                listener.enterSeries_connection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeries_connection" ):
                listener.exitSeries_connection(self)



    def connection(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cevParser.ConnectionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_connection, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = cevParser.ElementContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 9
            self.resistor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 16
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cevParser.Series_connectionContext(self, cevParser.ConnectionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_connection)
                    self.state = 11
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 12
                    self.match(cevParser.T__0)
                    self.state = 13
                    self.connection(3) 
                self.state = 18
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 4, self.RULE_resistor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            localctx.value = self.match(cevParser.NUMBER)
            self.state = 20
            self.match(cevParser.UNIT_RESISTOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.connection_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def connection_sempred(self, localctx:ConnectionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




