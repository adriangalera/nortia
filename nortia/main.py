import argparse
from multiprocessing import Process

from nortia.webserver import serve
from nortia.gpioinput import listen_gpio_events

def start_web(filename):
    serve(filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='nortia',
        description='Time management software')
    parser.add_argument('--filename', required=True)
    parser.add_argument('--led-pwr-pin', required=True)
    parser.add_argument('--btn-read-pin', required=True)
    args = parser.parse_args()

    process = Process(target=start_web, args=(args.filename,))
    process.start()

    listen_gpio_events(args.filename, args.led_pwr_pin, args.btn_read_pin)
