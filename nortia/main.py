import argparse
from multiprocessing import Process

from nortia.webserver import serve
from nortia.gpioinput import listen_gpio_events
from nortia.stdinput_reader import listen_input_events


def listen_web_async(filename):
    process = Process(target=serve, args=(filename,))
    process.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='nortia',
        description='Time management software')
    parser.add_argument('--filename', required=True)
    parser.add_argument('--led-pwr-pin', required=True,
                        type=int, choices=range(0, 10))
    parser.add_argument('--btn-read-pin', required=True,
                        type=int, choices=range(0, 10))
    args = parser.parse_args()

    listen_web_async(args.filename)
    # listen_gpio_events(args.filename, args.led_pwr_pin, args.btn_read_pin)
    listen_input_events(args.filename)
