import argparse

import repo


def read_input(filename):
    while True:
        input_str = input("IN/OUT: ")
        if "IN" in input_str:
            print("IN")
            repo.write_now_in(filename)
        else:
            print("OUT")
            repo.write_now_out(filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='nortia',
        description='Time management software')
    parser.add_argument('filename')
    args = parser.parse_args()

    read_input(args.filename)
