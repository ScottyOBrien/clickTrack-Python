import time
from pynput import keyboard
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import logging
import datetime
from datetime import datetime as datetime_time
import sys

# setting up datetime object and converting to string for file name
currentDate = datetime.date.today()
stringDate = currentDate.strftime("%m-%d-%Y")
scriptStartTime = datetime_time.now()

# variables for tracking clicks
leftClicks = 0
rightClicks = 0
totalClicks = 0

# input from user
print("The information you enter is used for the filename, don't use spaces or special characters that arent accepted "
      "for filenames.")
game = input("what game are you playing?: ")
character = input("what character?: ")
print("Logging.. Minimize this window until you are ready to stop the script.")
print("------------------------------------------------------------------------------")
print("shift+a+x to stop the script and save your clicks to the log.")
time.sleep(2)
print("Happy Clicking!")

# setup logfile
logging.basicConfig(filename=stringDate + "-" + game + "-" + character + "-clicks_log.txt", level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

# The key combination to check
COMBINATION = {keyboard.Key.shift, keyboard.KeyCode.from_char('A'), keyboard.KeyCode.from_char('X')}

# The currently active modifiers
current = set()


# methods for KEYBOARD listener
def on_press(key):
    global scriptStartTime
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            print('Saving file and ending script...')
            logging.info('Total Clicks: ' + str(totalClicks))
            logging.info('Left Clicks: ' + str(leftClicks))
            logging.info('Right Clicks: ' + str(rightClicks))
            scriptRunTime = datetime_time.now() - scriptStartTime
            logging.info("Script Run time: " + str(scriptRunTime))
            print("you may now close this window.")
            # print(datetime_time.now() - scriptStartTime)
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
