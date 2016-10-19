from pfc import io

class Lexer:

	def __init__(self, line_length):
		self.line_length = line_length
		self.errors = 0

	def __lineCount(self, stream):
		for index, line in enumerate(stream):
			yield index+1, line

	def __isComment(self, line):
		c = line[0]
		if c == 'C' or c == '*' or c == '!':
			return True
		return False

	def lex(self, stream):
		for index, line in self.__lineCount(stream):
			if len(line) <= self.line_length:
				if self.__isComment(line):
					continue
				print("not a comment")
			else:
				io.error(index, "Line too long: {} > {}".format(
					len(line), self.line_length))
				self.errors += 1
