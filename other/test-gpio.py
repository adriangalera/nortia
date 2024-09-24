import RPi.GPIO as GPIO
from time import sleep

BTN_READ_PIN = 3
LED_PWR_PIN = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(BTN_READ_PIN, GPIO.IN)
GPIO.setup(LED_PWR_PIN, GPIO.OUT)

previous_state = None
cur_state = None
while True:
    if GPIO.input(BTN_READ_PIN) == 1:
        cur_state = "OUT"
        GPIO.output(LED_PWR_PIN, False)
    else:
        cur_state = "IN"
        GPIO.output(LED_PWR_PIN, True)

    if previous_state is not None and previous_state != cur_state:
        print(cur_state)

    previous_state = cur_state
    sleep(0.25)
