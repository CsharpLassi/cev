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


    # Enter a parse tree produced by cevParser#parallel_connection.
    def enterParallel_connection(self, ctx:cevParser.Parallel_connectionContext):
        pass

    # Exit a parse tree produced by cevParser#parallel_connection.
    def exitParallel_connection(self, ctx:cevParser.Parallel_connectionContext):
        pass


    # Enter a parse tree produced by cevParser#element.
    def enterElement(self, ctx:cevParser.ElementContext):
        pass

    # Exit a parse tree produced by cevParser#element.
    def exitElement(self, ctx:cevParser.ElementContext):
        pass


    # Enter a parse tree produced by cevParser#series_connection.
    def enterSeries_connection(self, ctx:cevParser.Series_connectionContext):
        pass

    # Exit a parse tree produced by cevParser#series_connection.
    def exitSeries_connection(self, ctx:cevParser.Series_connectionContext):
        pass


    # Enter a parse tree produced by cevParser#resistor.
    def enterResistor(self, ctx:cevParser.ResistorContext):
        pass

    # Exit a parse tree produced by cevParser#resistor.
    def exitResistor(self, ctx:cevParser.ResistorContext):
        pass


