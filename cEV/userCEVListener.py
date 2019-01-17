from cEV.OpCodes import OpCodes
from cEV.gen.cevListener import cevListener
from cEV.gen.cevParser import cevParser


class UserCEVListener(cevListener):
    def __init__(self):
        self.code = list()

    def exitResistor(self, ctx: cevParser.ResistorContext):
        self.code.append(OpCodes.CREATE_RESISTOR)
        self.code.append(float(ctx.value.text))
        self.code.append(OpCodes.SET_VALUE)

    def exitSeries_connection(self, ctx: cevParser.Series_connectionContext):
        self.code.append(OpCodes.CALC_SERIES)
