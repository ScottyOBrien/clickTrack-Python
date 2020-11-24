from threading import Lock

import pynput
from pynput import mouse
import logging
import datetime
from datetime import datetime as datetime_time
import tkinter as tk
import clicks

# initialize our clicks object
click = clicks.Clicks()


def on_click(x, y, button, pressed):
    currentClick = '{2}'.format(x, y, button)
    if pressed:
        print(click.public_totalClicks, click.public_rightClicks, click.public_leftClicks)
        if currentClick == 'Button.left':
            click.increment_left()
        if currentClick == 'Button.right':
            click.increment_right()
        click.increment_total()


# listener threads
listener = mouse.Listener(on_click=on_click)
listener.start()


def end_logging():
    print('Saving file and ending script...')
    logging.info('Total Clicks: ' + str(click.public_totalClicks))
    logging.info('Left Clicks: ' + str(click.public_leftClicks))
    logging.info('Right Clicks: ' + str(click.public_rightClicks))
    scriptRunTime = datetime_time.now() - scriptStartTime
    logging.info("Script Run time: " + str(scriptRunTime))
    click.set_right(0)
    click.set_left(0)
    click.set_total(0)


def copy_jason():
    window.clipboard_clear()


def begin_logging():
    click.set_right(0)
    click.set_left(0)
    click.set_total(0)
    global scriptStartTime
    # setting up datetime object and converting to string for file name
    currentDate = datetime.date.today()
    stringDate = currentDate.strftime("%m-%d-%Y")
    scriptStartTime = datetime_time.now()

    # setup logfile
    logging.basicConfig(filename=stringDate + "-clicks_log.txt", level=logging.DEBUG,
                        format='%(asctime)s: %(message)s')


# clear entry fields
def clear_entries():
    gameEntry.delete(0, 'end')
    characterEntry.delete(0, 'end')


window = tk.Tk()
window.title("ClickTrack")

# Create the frame
frm_info = tk.Frame(relief=tk.SUNKEN, borderwidth=4)
frm_info.pack()

# Create label/entry box and place them in the frame
gameLabel = tk.Label(master=frm_info, text="Game Title")
gameEntry = tk.Entry(master=frm_info, width=50)
gameLabel.grid(row=0, column=0, sticky="e")
gameEntry.grid(row=0, column=1)

# Create label/entry box and place them in the frame
characterLabel = tk.Label(master=frm_info, text="Character")
characterEntry = tk.Entry(master=frm_info, width=50)
characterLabel.grid(row=1, column=0, sticky="e")
characterEntry.grid(row=1, column=1)

# Create a new frame `frm_buttons` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Create the "run" button and pack it to the
# right side of `frm_buttons`
btn_run = tk.Button(master=frm_buttons, text="Run", command=begin_logging)
btn_run.pack(side=tk.LEFT, padx=10, ipadx=10)

# Create the "Clear" button and pack it to the
# right side of `frm_buttons`
btn_clear = tk.Button(master=frm_buttons, text="Clear", command=clear_entries)
btn_clear.pack(side=tk.LEFT, ipadx=10)

# Create button to finish logging data
# right side of 'frm_buttons'
btn_finish = tk.Button(master=frm_buttons, text="Finish", command=end_logging)
btn_finish.pack(side=tk.LEFT, padx=10, ipadx=10)

# Create the disabled text widget that will hold the JSON for the user to copy
# placement should be below the clear/run buttons.


# Start the application
window.mainloop()
