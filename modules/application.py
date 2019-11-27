from .handler import TextHandler
from .generator import Generator


class Application:
    """
    Application for text preprocessing and audio generation
    """
    def __init__(self, textpath: str, mp3path: str):
        self.handler = TextHandler(textpath)
        self.generator = Generator(mp3path)

    def start(self):
        """
        Launch app
        :return: None
        """
        prepared_text = self.handler.get_prepared_text()
        self.generator.create_audio(prepared_text)
