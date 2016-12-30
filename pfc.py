#!/usr/bin/env python3

import argparse
from pfc import lexer


def main(arguments):
	lex = lexer.Lexer(arguments.line_length)
	with open(arguments.source, "r") as src_stream:
		lex.lex(src_stream)
	#parser = Parser(lex.getToken())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FORTRAN I Compiler")
    parser.add_argument("source", type=str, help="source file")
	parser.add_argument(
		"--line-length", type=int, default=72,
		help="change max line lenght (default: 72)"
	)
	parser.add_argument("-o", "--output", help="output file")
	args = parser.parse_args()
	main(args)
