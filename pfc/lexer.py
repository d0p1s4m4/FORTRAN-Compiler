from pfc import io

class Lexer:

	WHITESPACE = [' ', '\t']

	def __init__(self, line_length):
		self.line_length = line_length
		self.errors = 0
		self.tokens = dict()

	def __lineCount(self, stream):
		for index, line in enumerate(stream):
			yield index+1, line

	def __isComment(self, line, index):
		c = line[0]
		if c == 'C' or c == '*' or c == '!':
			return True
		if c not in Lexer.WHITESPACE:
			io.error(index,
				"Column 0 must be a whitespace \
(found '{}' instead)".format(c))
			self.errors += 1
		return False

	def pushToken(self, token, lineno):
		if not lineno in self.tokens:
			self.tokens[lineno] = list()
		self.tokens[lineno].apppend(token)

	def lex(self, stream):
		for index, line in self.__lineCount(stream):
			if len(line) <= self.line_length:
				if self.__isComment(line, index):
					continue
				print(line)
			else:
				io.error(index, "Line too long: {} > {}".format(
					len(line), self.line_length))
				self.errors += 1
