import argparse

from modules.application import Application

# Set args parser
parser = argparse.ArgumentParser(description='Yandex Speech Generator')
parser.add_argument('--textpath', help='Path of input .txt file')
parser.add_argument('--mp3path', help='Path of outout .mp3 file')
args = parser.parse_args()


if __name__ == '__main__':
    app = Application(textpath=args.textpath, mp3path=args.mp3path)
    app.start()

