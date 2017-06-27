import os


class SourceStream(object):

    def __init__(self, file):
        self.file = file
        self.name = os.path.basename(file)
        self.lineno = 0
        if not os.path.isfile(file):
            raise FileNotFoundError()

    def read_line(self) -> str:
        for index, line in enumerate(self.__stream, 1):
            self.lineno = index
            yield line

    def close(self) -> None:
        self.__stream.close()

    def __enter__(self):
        self.__stream = open(self.file, "r")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
