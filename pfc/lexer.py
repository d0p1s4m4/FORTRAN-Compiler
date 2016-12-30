import re
from pfc.utils import io
from pfc.utils.constants import *


class Lexer:

    LINE_MAX_LENGTH = 72
    WHITESPACE = ' '
    RE_VALID_CHAR = re.compile(r"^[0-9 A-Z*=/+.(),-]+$")
    RE_STATEMENT_NUMBER = re.compile(r"^(?:\s+)?([0-9]+)?(?:\s+)?$")
    KEYWORDS = ["GO", "TO", "ASSIGN", "IF", "SENSE", "LIGHT", "ACCUMULATOR",
                "OVERFLOW", "QUOTIENT", "DIVIDE", "CHECK", "PAUSE", "FORMAT",
                "READ", "INPUT", "TAPE", "PUNCH", "PRINT", "WRITE", "DRUM",
                "END", "FILE", "REWIND", "BACKSPACE", "CONTINUE", "DIMENSION",
                "EQUIVALENCE", "FREQUENCY"]

    def __init__(self):
        self.errors = 0
        self.tokens = dict()

    def __push_token(self, token: tuple, stream) -> None:
        if stream.file not in self.tokens.keys():
            self.tokens[stream.file] = dict()
        if stream.lineno not in self.tokens[stream.file].keys():
            self.tokens[stream.file][stream.lineno] = list()
        self.tokens[stream.file][stream.lineno].append(token)

    def __is_comment(self, col0: str, stream) -> bool:
        if col0 == 'C':
            return True
        if col0 not in Lexer.WHITESPACE:
            self.errors += 1
            io.error(stream.file, stream.lineno,
                     ERR_COMMENT_COL.format(col0))
        return False

    def __check_statement_number(self, col1to5: str, stream) -> None:
        result = Lexer.RE_STATEMENT_NUMBER.match(col1to5)
        if not result:
            self.errors += 1
            io.error(stream.file, stream.lineno, ERR_NUMBER_STATEMENT_COL)
            return
        if result.group(1):
            self.__push_token(("LINE_LABEL", result.group(1)), stream)

    def __check_continuation(self, col6: str, stream) -> None:
        if col6 != Lexer.WHITESPACE:
            self.__push_token(("LINE_CONTINUATION", None), stream)

    def __lex_statement(self, line: str, stream) -> None:
        while len(line) > 0:
            pass

    def lex(self, stream):
        for line in stream.read_line():
            if len(line) > Lexer.LINE_MAX_LENGTH:
                self.errors += 1
                io.error(stream.file, stream.lineno,
                         ERR_LINE_LENGTH.format(len(line)))
                continue
            if not Lexer.RE_VALID_CHAR.match(line):
                self.errors += 1
                io.error(stream.file, stream.lineno, ERR_INCORRECT_CHAR)
            if self.__is_comment(line, stream):
                continue
            self.__check_statement_number(line[1:5], stream)
            self.__check_continuation(line[6], stream)
            self.__lex_statement(line[7:], stream)
