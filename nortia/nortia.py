import argparse
from multiprocessing import Process

import repo
import webserver


def read_input(filename):
    while True:
        input_str = input("IN/OUT: ")
        if "IN" in input_str:
            print("IN")
            repo.write_now_in(filename)
        else:
            print("OUT")
            repo.write_now_out(filename)

def start_web(filename):
    webserver.serve(filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='nortia',
        description='Time management software')
    parser.add_argument('filename')
    args = parser.parse_args()


    process = Process(target=start_web, args=(args.filename,))
    process.start()

    read_input(args.filename)

    #swebserver.serve(args.filename)
    #s# TODO: Replace by the button thread
    #read_input(args.filename)
