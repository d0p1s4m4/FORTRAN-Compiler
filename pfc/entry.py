import argparse
from pfc.lexer import Lexer
from pfc.src.source_stream import SourceStream


def main() -> int:
    cli_parser = argparse.ArgumentParser(description="FORTRAN I Compiler")

    cli_parser.add_argument("source", type=str, help="source file")
    cli_parser.add_argument("-o", "--output", help="output file")

    args = cli_parser.parse_args()

    lexer = Lexer()
    with SourceStream(args.source) as stream:
        tokens, errors = lexer.lex(stream)
    print(tokens)
