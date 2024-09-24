from time import sleep
#from RPi import GPIO # pylint: disable=import-error

from nortia.repo import write_now_in, write_now_out


def state_has_changed(previous_state, cur_state):
    return previous_state is not None and previous_state != cur_state


def listen_gpio_events(filename, led_pwr_pin, btn_read_pin):
    print(f"GPIO listening for events at pin {btn_read_pin}")

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(btn_read_pin, GPIO.IN)
    GPIO.setup(led_pwr_pin, GPIO.OUT)

    previous_state = None
    cur_state = None
    while True:
        if GPIO.input(btn_read_pin) == 1:
            cur_state = "OUT"
            GPIO.output(led_pwr_pin, False)
        else:
            cur_state = "IN"
            GPIO.output(led_pwr_pin, True)

        if state_has_changed(previous_state, cur_state):
            if cur_state == "IN":
                write_now_in(filename)
            else:
                write_now_out(filename)

        previous_state = cur_state
        sleep(0.25)
