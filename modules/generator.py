import os

import requests
from pydub import AudioSegment

from .base import BaseApplication


class Generator(BaseApplication):
    def __init__(self, filename: str):
        """
        Audio generator, works with Yandex API
        :param filename: output filename
        """
        super().__init__()
        self.filename = filename.replace('.mp3', '')

    def __synthesize(self, text: str) -> bytes:
        """
        :param text: chunked text
        :return: generated part in bytes
        """
        url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
        headers = {
            'Authorization': 'Bearer ' + self.config['yandex_api_token'],
        }

        data = {
            'text': text,
            'lang': 'ru-RU',
            'folderId': self.config['yandex_api_cat']
        }

        with requests.post(url, headers=headers, data=data, stream=True) as resp:
            if resp.status_code != 200:
                raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

            for chunk in resp.iter_content(chunk_size=None):
                yield chunk

    def __convert_audio(self):
        """
        Convert .ogg file from Yandex API to .mp3 file
        :return: None
        """
        AudioSegment.from_ogg(self.filename + '.ogg').export(self.filename + '.mp3')
        os.remove(self.filename + '.ogg')

    def create_audio(self, prepared_text):
        """
        Generate audio from Yandex API and convert it to .mp3
        :param prepared_text: chunked text
        :return: None
        """
        with open(self.filename + '.ogg', "wb") as f:
            for text_part in prepared_text:
                for audio_content in self.__synthesize(text_part):
                    f.write(audio_content)

        print('Converting to mp3...')
        self.__convert_audio()
        print('Finished!')
