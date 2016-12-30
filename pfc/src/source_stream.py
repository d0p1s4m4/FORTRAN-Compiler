import os
from pfc.utils import io
from pfc.utils import constants


class SourceStream(object):

    def __init__(self, file):
        self.name = os.path.basename(file)
        self.lineno = 0
        if not os.path.isfile(file):
            io.error(self.name, self.lineno, constants.ERR_FILE_NOT_FOUND)
            raise FileNotFoundError()
        self.__stream = open(file, "r")

    def read_line(self) -> str:
        for index, line in enumerate(self.__stream, 1):
            self.lineno = index
            yield line

    def close(self) -> None:
        self.__stream.close()
