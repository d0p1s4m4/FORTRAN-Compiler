from pfc.src.source_stream import SourceStream


class SourceFile(object):

    def __init__(self, file):
        self.__stream = SourceStream(file)

    def __enter__(self):
        return self.__stream

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__stream.close()