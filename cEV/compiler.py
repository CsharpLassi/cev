from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from cEV.machine import Machine
from cEV.gen.cevLexer import cevLexer
from cEV.gen.cevParser import cevParser
from cEV.userCEVListener import UserCEVListener


class CEVCompiler:
    def compileLine(self, line: str):
        input = InputStream(line)
        lexer = cevLexer(input)
        stream = CommonTokenStream(lexer)
        parser = cevParser(stream)
        tree = parser.stmt()

        listener = UserCEVListener()
        walker = ParseTreeWalker()

        walker.walk(listener, tree)

        return listener.code

    def executeLine(self, line: str):
        code = self.compileLine(line)

        machine = Machine(code)
        machine.run()
        return machine.pop()

