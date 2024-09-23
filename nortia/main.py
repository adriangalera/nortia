import argparse
from multiprocessing import Process

from nortia.webserver import serve
from nortia.input_reader import read_input


def start_web(filename):
    serve(filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='nortia',
        description='Time management software')
    parser.add_argument('filename')
    args = parser.parse_args()

    process = Process(target=start_web, args=(args.filename,))
    process.start()

    read_input(args.filename)
