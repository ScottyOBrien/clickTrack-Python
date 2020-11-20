from pynput import keyboard
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import logging
import datetime
import sys

# setting up datetime object and converting to string for file name
currentDate = datetime.date.today()
stringDate = currentDate.strftime("%m-%d-%Y")

# variables for tracking clicks
leftClicks = 0
rightClicks = 0
totalClicks = 0

# setup logfile
logging.basicConfig(filename=stringDate + "-clicks_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

# The key combination to check
COMBINATION = {keyboard.Key.shift, keyboard.KeyCode.from_char('A'), keyboard.KeyCode.from_char('X')}

# The currently active modifiers
current = set()


# methods for KEYBOARD listener
def on_press(key):
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            print('All modifiers active!')
            logging.info('Total Clicks: ' + str(totalClicks))
            logging.info('Left Clicks: ' + str(leftClicks))
            logging.info('Right Clicks: ' + str(rightClicks))
            sys.exit()

    if key == keyboard.Key.esc:
        print("stopping")
        keyboard_listener.stop()
        sys.exit()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


# methods for MOUSE Listener
def on_click(x, y, button, pressed):
    global totalClicks
    global leftClicks
    global rightClicks
    currentClick = '{2}'.format(x, y, button)
    if pressed:
        if currentClick == 'Button.left':
            leftClicks += 1
        if currentClick == 'Button.right':
            rightClicks += 1
        totalClicks += 1


# listener threads
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
mouse_listener = MouseListener(on_click=on_click)

# start/join threads so script doesnt end early
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()
