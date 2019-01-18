# Generated from /home/lassi/Dokumente/develop/cEV/cEV/cev.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cevParser import cevParser
else:
    from cevParser import cevParser

# This class defines a complete listener for a parse tree produced by cevParser.
class cevListener(ParseTreeListener):

    # Enter a parse tree produced by cevParser#stmt.
    def enterStmt(self, ctx:cevParser.StmtContext):
        pass

    # Exit a parse tree produced by cevParser#stmt.
    def exitStmt(self, ctx:cevParser.StmtContext):
        pass


    # Enter a parse tree produced by cevParser#function.
    def enterFunction(self, ctx:cevParser.FunctionContext):
        pass

    # Exit a parse tree produced by cevParser#function.
    def exitFunction(self, ctx:cevParser.FunctionContext):
        pass


    # Enter a parse tree produced by cevParser#voltageFunction.
    def enterVoltageFunction(self, ctx:cevParser.VoltageFunctionContext):
        pass

    # Exit a parse tree produced by cevParser#voltageFunction.
    def exitVoltageFunction(self, ctx:cevParser.VoltageFunctionContext):
        pass


    # Enter a parse tree produced by cevParser#connectionComponent.
    def enterConnectionComponent(self, ctx:cevParser.ConnectionComponentContext):
        pass

    # Exit a parse tree produced by cevParser#connectionComponent.
    def exitConnectionComponent(self, ctx:cevParser.ConnectionComponentContext):
        pass


    # Enter a parse tree produced by cevParser#parallel_connection.
    def enterParallel_connection(self, ctx:cevParser.Parallel_connectionContext):
        pass

    # Exit a parse tree produced by cevParser#parallel_connection.
    def exitParallel_connection(self, ctx:cevParser.Parallel_connectionContext):
        pass


    # Enter a parse tree produced by cevParser#series_connection.
    def enterSeries_connection(self, ctx:cevParser.Series_connectionContext):
        pass

    # Exit a parse tree produced by cevParser#series_connection.
    def exitSeries_connection(self, ctx:cevParser.Series_connectionContext):
        pass


    # Enter a parse tree produced by cevParser#resistorComponent.
    def enterResistorComponent(self, ctx:cevParser.ResistorComponentContext):
        pass

    # Exit a parse tree produced by cevParser#resistorComponent.
    def exitResistorComponent(self, ctx:cevParser.ResistorComponentContext):
        pass


    # Enter a parse tree produced by cevParser#voltageSourceComponent.
    def enterVoltageSourceComponent(self, ctx:cevParser.VoltageSourceComponentContext):
        pass

    # Exit a parse tree produced by cevParser#voltageSourceComponent.
    def exitVoltageSourceComponent(self, ctx:cevParser.VoltageSourceComponentContext):
        pass


    # Enter a parse tree produced by cevParser#parameterList.
    def enterParameterList(self, ctx:cevParser.ParameterListContext):
        pass

    # Exit a parse tree produced by cevParser#parameterList.
    def exitParameterList(self, ctx:cevParser.ParameterListContext):
        pass


    # Enter a parse tree produced by cevParser#currentParameter.
    def enterCurrentParameter(self, ctx:cevParser.CurrentParameterContext):
        pass

    # Exit a parse tree produced by cevParser#currentParameter.
    def exitCurrentParameter(self, ctx:cevParser.CurrentParameterContext):
        pass


    # Enter a parse tree produced by cevParser#resistor.
    def enterResistor(self, ctx:cevParser.ResistorContext):
        pass

    # Exit a parse tree produced by cevParser#resistor.
    def exitResistor(self, ctx:cevParser.ResistorContext):
        pass


    # Enter a parse tree produced by cevParser#voltage.
    def enterVoltage(self, ctx:cevParser.VoltageContext):
        pass

    # Exit a parse tree produced by cevParser#voltage.
    def exitVoltage(self, ctx:cevParser.VoltageContext):
        pass


    # Enter a parse tree produced by cevParser#current.
    def enterCurrent(self, ctx:cevParser.CurrentContext):
        pass

    # Exit a parse tree produced by cevParser#current.
    def exitCurrent(self, ctx:cevParser.CurrentContext):
        pass


