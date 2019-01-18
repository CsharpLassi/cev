# Generated from /home/lassi/Dokumente/develop/cEV/cEV/cev.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("#\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\5\2\r\n\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\30\n\3\f\3\16\3")
        buf.write("\33\13\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\2\3\4\6\2\4\6\b\2")
        buf.write("\2\2!\2\f\3\2\2\2\4\16\3\2\2\2\6\34\3\2\2\2\b\37\3\2\2")
        buf.write("\2\n\r\5\4\3\2\13\r\5\b\5\2\f\n\3\2\2\2\f\13\3\2\2\2\r")
        buf.write("\3\3\2\2\2\16\17\b\3\1\2\17\20\5\6\4\2\20\31\3\2\2\2\21")
        buf.write("\22\f\5\2\2\22\23\7\3\2\2\23\30\5\4\3\6\24\25\f\4\2\2")
        buf.write("\25\26\7\4\2\2\26\30\5\4\3\5\27\21\3\2\2\2\27\24\3\2\2")
        buf.write("\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\5\3\2")
        buf.write("\2\2\33\31\3\2\2\2\34\35\7\5\2\2\35\36\7\6\2\2\36\7\3")
        buf.write("\2\2\2\37 \7\5\2\2 !\7\7\2\2!\t\3\2\2\2\5\f\27\31")
        return buf.getvalue()


class cevParser ( Parser ):

    grammarFileName = "cev.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'||'", "<INVALID>", "<INVALID>", 
                     "'V'", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "UNIT_RESISTOR", 
                      "UNIT_VOLTAGE", "WHITESPACE" ]

    RULE_stmt = 0
    RULE_connection = 1
    RULE_resistor = 2
    RULE_voltage = 3

    ruleNames =  [ "stmt", "connection", "resistor", "voltage" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NUMBER=3
    UNIT_RESISTOR=4
    UNIT_VOLTAGE=5
    WHITESPACE=6

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


        def voltage(self):
            return self.getTypedRuleContext(cevParser.VoltageContext,0)


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
            self.state = 10
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.connection(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.voltage()
                pass


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


    class Parallel_connectionContext(ConnectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cevParser.ConnectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def connection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cevParser.ConnectionContext)
            else:
                return self.getTypedRuleContext(cevParser.ConnectionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParallel_connection" ):
                listener.enterParallel_connection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParallel_connection" ):
                listener.exitParallel_connection(self)


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

            self.state = 13
            self.resistor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 21
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = cevParser.Series_connectionContext(self, cevParser.ConnectionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_connection)
                        self.state = 15
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 16
                        self.match(cevParser.T__0)
                        self.state = 17
                        self.connection(4)
                        pass

                    elif la_ == 2:
                        localctx = cevParser.Parallel_connectionContext(self, cevParser.ConnectionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_connection)
                        self.state = 18
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 19
                        self.match(cevParser.T__1)
                        self.state = 20
                        self.connection(3)
                        pass

             
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
            self.state = 26
            localctx.value = self.match(cevParser.NUMBER)
            self.state = 27
            self.match(cevParser.UNIT_RESISTOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoltageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None # Token

        def UNIT_VOLTAGE(self):
            return self.getToken(cevParser.UNIT_VOLTAGE, 0)

        def NUMBER(self):
            return self.getToken(cevParser.NUMBER, 0)

        def getRuleIndex(self):
            return cevParser.RULE_voltage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoltage" ):
                listener.enterVoltage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoltage" ):
                listener.exitVoltage(self)




    def voltage(self):

        localctx = cevParser.VoltageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_voltage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            localctx.value = self.match(cevParser.NUMBER)
            self.state = 30
            self.match(cevParser.UNIT_VOLTAGE)
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
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




