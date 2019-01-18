# Generated from /home/lassi/Dokumente/develop/cEV/cEV/cev.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\5\2\31\n\2\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\7\5,\n\5\f\5\16\5/\13\5\3\6\3\6\5\6\63\n\6")
        buf.write("\3\7\3\7\7\7\67\n\7\f\7\16\7:\13\7\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\2\3\b\f\2\4\6")
        buf.write("\b\n\f\16\20\22\24\2\2\2C\2\30\3\2\2\2\4\32\3\2\2\2\6")
        buf.write("\34\3\2\2\2\b\"\3\2\2\2\n\62\3\2\2\2\f8\3\2\2\2\16;\3")
        buf.write("\2\2\2\20?\3\2\2\2\22B\3\2\2\2\24E\3\2\2\2\26\31\5\b\5")
        buf.write("\2\27\31\5\4\3\2\30\26\3\2\2\2\30\27\3\2\2\2\31\3\3\2")
        buf.write("\2\2\32\33\5\6\4\2\33\5\3\2\2\2\34\35\7\3\2\2\35\36\7")
        buf.write("\4\2\2\36\37\5\b\5\2\37 \5\f\7\2 !\7\5\2\2!\7\3\2\2\2")
        buf.write("\"#\b\5\1\2#$\5\n\6\2$-\3\2\2\2%&\f\5\2\2&\'\7\6\2\2\'")
        buf.write(",\5\b\5\6()\f\4\2\2)*\7\7\2\2*,\5\b\5\5+%\3\2\2\2+(\3")
        buf.write("\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\t\3\2\2\2/-\3\2")
        buf.write("\2\2\60\63\5\20\t\2\61\63\5\22\n\2\62\60\3\2\2\2\62\61")
        buf.write("\3\2\2\2\63\13\3\2\2\2\64\65\7\b\2\2\65\67\5\16\b\2\66")
        buf.write("\64\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29\r\3\2\2")
        buf.write("\2:8\3\2\2\2;<\7\t\2\2<=\7\n\2\2=>\5\24\13\2>\17\3\2\2")
        buf.write("\2?@\7\13\2\2@A\7\f\2\2A\21\3\2\2\2BC\7\13\2\2CD\7\r\2")
        buf.write("\2D\23\3\2\2\2EF\7\13\2\2FG\7\16\2\2G\25\3\2\2\2\7\30")
        buf.write("+-\628")
        return buf.getvalue()


class cevParser ( Parser ):

    grammarFileName = "cev.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'U'", "'('", "')'", "'+'", "'||'", "','", 
                     "'I'", "'='", "<INVALID>", "<INVALID>", "'V'", "'A'", 
                     "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "UNIT_RESISTOR", "UNIT_VOLTAGE", 
                      "UNIT_CURRENT", "WHITESPACE" ]

    RULE_stmt = 0
    RULE_function = 1
    RULE_voltageFunction = 2
    RULE_connection = 3
    RULE_components = 4
    RULE_parameterList = 5
    RULE_currentParameter = 6
    RULE_resistor = 7
    RULE_voltage = 8
    RULE_current = 9

    ruleNames =  [ "stmt", "function", "voltageFunction", "connection", 
                   "components", "parameterList", "currentParameter", "resistor", 
                   "voltage", "current" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NUMBER=9
    UNIT_RESISTOR=10
    UNIT_VOLTAGE=11
    UNIT_CURRENT=12
    WHITESPACE=13

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


        def function(self):
            return self.getTypedRuleContext(cevParser.FunctionContext,0)


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
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cevParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.connection(0)
                pass
            elif token in [cevParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.function()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def voltageFunction(self):
            return self.getTypedRuleContext(cevParser.VoltageFunctionContext,0)


        def getRuleIndex(self):
            return cevParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = cevParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.voltageFunction()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoltageFunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def connection(self):
            return self.getTypedRuleContext(cevParser.ConnectionContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(cevParser.ParameterListContext,0)


        def getRuleIndex(self):
            return cevParser.RULE_voltageFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoltageFunction" ):
                listener.enterVoltageFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoltageFunction" ):
                listener.exitVoltageFunction(self)




    def voltageFunction(self):

        localctx = cevParser.VoltageFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_voltageFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(cevParser.T__0)
            self.state = 27
            self.match(cevParser.T__1)
            self.state = 28
            self.connection(0)
            self.state = 29
            self.parameterList()
            self.state = 30
            self.match(cevParser.T__2)
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


    class ConnectionComponentContext(ConnectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cevParser.ConnectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def components(self):
            return self.getTypedRuleContext(cevParser.ComponentsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConnectionComponent" ):
                listener.enterConnectionComponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConnectionComponent" ):
                listener.exitConnectionComponent(self)


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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_connection, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = cevParser.ConnectionComponentContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 33
            self.components()
            self._ctx.stop = self._input.LT(-1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 41
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = cevParser.Series_connectionContext(self, cevParser.ConnectionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_connection)
                        self.state = 35
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 36
                        self.match(cevParser.T__3)
                        self.state = 37
                        self.connection(4)
                        pass

                    elif la_ == 2:
                        localctx = cevParser.Parallel_connectionContext(self, cevParser.ConnectionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_connection)
                        self.state = 38
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 39
                        self.match(cevParser.T__4)
                        self.state = 40
                        self.connection(3)
                        pass

             
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComponentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cevParser.RULE_components

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VoltageSourceComponentContext(ComponentsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cevParser.ComponentsContext
            super().__init__(parser)
            self.element = None # VoltageContext
            self.copyFrom(ctx)

        def voltage(self):
            return self.getTypedRuleContext(cevParser.VoltageContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoltageSourceComponent" ):
                listener.enterVoltageSourceComponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoltageSourceComponent" ):
                listener.exitVoltageSourceComponent(self)


    class ResistorComponentContext(ComponentsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cevParser.ComponentsContext
            super().__init__(parser)
            self.element = None # ResistorContext
            self.copyFrom(ctx)

        def resistor(self):
            return self.getTypedRuleContext(cevParser.ResistorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResistorComponent" ):
                listener.enterResistorComponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResistorComponent" ):
                listener.exitResistorComponent(self)



    def components(self):

        localctx = cevParser.ComponentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_components)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = cevParser.ResistorComponentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                localctx.element = self.resistor()
                pass

            elif la_ == 2:
                localctx = cevParser.VoltageSourceComponentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                localctx.element = self.voltage()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def currentParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cevParser.CurrentParameterContext)
            else:
                return self.getTypedRuleContext(cevParser.CurrentParameterContext,i)


        def getRuleIndex(self):
            return cevParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = cevParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cevParser.T__5:
                self.state = 50
                self.match(cevParser.T__5)
                self.state = 51
                self.currentParameter()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CurrentParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.parameter = None # CurrentContext

        def current(self):
            return self.getTypedRuleContext(cevParser.CurrentContext,0)


        def getRuleIndex(self):
            return cevParser.RULE_currentParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCurrentParameter" ):
                listener.enterCurrentParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCurrentParameter" ):
                listener.exitCurrentParameter(self)




    def currentParameter(self):

        localctx = cevParser.CurrentParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_currentParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(cevParser.T__6)
            self.state = 58
            self.match(cevParser.T__7)
            self.state = 59
            localctx.parameter = self.current()
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
        self.enterRule(localctx, 14, self.RULE_resistor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            localctx.value = self.match(cevParser.NUMBER)
            self.state = 62
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
        self.enterRule(localctx, 16, self.RULE_voltage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            localctx.value = self.match(cevParser.NUMBER)
            self.state = 65
            self.match(cevParser.UNIT_VOLTAGE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CurrentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None # Token

        def UNIT_CURRENT(self):
            return self.getToken(cevParser.UNIT_CURRENT, 0)

        def NUMBER(self):
            return self.getToken(cevParser.NUMBER, 0)

        def getRuleIndex(self):
            return cevParser.RULE_current

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCurrent" ):
                listener.enterCurrent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCurrent" ):
                listener.exitCurrent(self)




    def current(self):

        localctx = cevParser.CurrentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_current)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            localctx.value = self.match(cevParser.NUMBER)
            self.state = 68
            self.match(cevParser.UNIT_CURRENT)
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
        self._predicates[3] = self.connection_sempred
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
         




