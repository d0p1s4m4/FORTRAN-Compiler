import sys

def __write(stream, msg, mark=""):
	stream.write("[\033[1m{}\033[0m] {}\n".format(mark, msg))

def error(lineno, msg):
	__write(sys.stderr, "\033[31mError\033[0m (L{}): {}".format(
		lineno, msg), "\033[31m-")
