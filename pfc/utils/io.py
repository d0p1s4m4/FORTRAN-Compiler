import sys


def error(file: str, lineno: int, msg: str) -> None:
    print("\033[31mError\033[0m [{}:L{}]: {}".format(
        file, lineno, msg
    ), file=sys.stderr)
