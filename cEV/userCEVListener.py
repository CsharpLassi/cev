from cEV.OpCodes import OpCodes
from cEV.gen.cevListener import cevListener
from cEV.gen.cevParser import cevParser


class UserCEVListener(cevListener):
    def __init__(self):
        self.code = list()

    def exitResistorComponent(self, ctx: cevParser.ResistorComponentContext):
        self.code.append(OpCodes.CREATE_RESISTOR)
        self.code.append(float(ctx.element.value.text))
        self.code.append(OpCodes.SET_VALUE)

    def exitVoltageSourceComponent(self, ctx: cevParser.VoltageSourceComponentContext):
        self.code.append(OpCodes.CREATE_VOLTAGESOURCE)
        self.code.append(float(ctx.element.value.text))
        self.code.append(OpCodes.SET_VALUE)

    def exitSeries_connection(self, ctx: cevParser.Series_connectionContext):
        self.code.append(OpCodes.CALC_SERIES)

    def exitParallel_connection(self, ctx: cevParser.Parallel_connectionContext):
        self.code.append(OpCodes.CALC_PARALLEL)

    def enterParameterList(self, ctx:cevParser.ParameterListContext):
        self.code.append(OpCodes.CREATE_DICT)

    def exitCurrentParameter(self, ctx: cevParser.CurrentParameterContext):
        self.code.append("i")
        self.code.append(float(ctx.parameter.value.text))
        self.code.append(OpCodes.ADD_KEY_VALUE)

    def exitVoltageFunction(self, ctx:cevParser.VoltageFunctionContext):
        self.code.append(OpCodes.CALC_VOLTAGE)
