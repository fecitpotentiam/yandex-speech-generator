import math
import textwrap

LIMIT = 5000


class TextHandler:
    def __init__(self, filename: str):
        """
        Handler of input text
        :param filename: input filename
        """
        self.filename = filename

    @staticmethod
    def __get_text(filename: str) -> str:
        with open(filename, 'r') as f:
            return f.read()

    def get_prepared_text(self) -> list:
        """
        Split text from file to chunks
        :return: list of chunked text
        """
        raw_text = self.__get_text(self.filename)

        chunks_count = len(raw_text) / math.ceil(len(raw_text) / LIMIT)

        return textwrap.wrap(raw_text, chunks_count)


if __name__ == '__main__':
    th = TextHandler('dfd')

