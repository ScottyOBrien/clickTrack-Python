import pynput
from pynput import mouse
import logging
import datetime
from datetime import datetime as datetime_time
import tkinter as tk
import clicks
import json

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
    # variables for cleanliness
    total = str(click.public_totalClicks)
    left = str(click.public_leftClicks)
    right = str(click.public_rightClicks)

    # console statement for debugging
    print('Saving file and ending script...')

    # add info to logfile
    logging.info('Total Clicks: ' + total)
    logging.info('Left Clicks: ' + left)
    logging.info('Right Clicks: ' + right)
    scriptRunTime = datetime_time.now() - scriptStartTime
    logging.info("Script Run time: " + str(scriptRunTime))

    # build the json, convert it with json.loads, add it to the text box and disable so its not editable
    data = build_json(total, left, right, scriptRunTime)
    logging.info(data)
    json_box['state'] = ['normal']
    json_box.insert('end', data)
    json_box['state'] = ['disabled']

    # re-enable run button
    btn_run['state'] = ['normal']


# Builds JSON from data gathered during listening
def build_json(tc, lc, rc, runtime):
    jsonData = "{\"data\": {\"game\":\"" + gameEntry.get() + "\", \"character\":\"" + characterEntry.get() + \
               "\", \"runtime\":\"" + str(runtime) + "\", \"clicks\": {" "\"totalClicks\":" + tc + ", \"leftClicks\":" + \
               lc + ", \"rightClicks\":" + rc + "}}} "
    convert = json.loads(jsonData)
    return convert


# copies JSON data to clipobard
def copy_json():
    window.clipboard_clear()
    window.clipboard_append(json_box.get("1.0", "end"))


# Resets counters, creates log file
def begin_logging():
    btn_run['state'] = ['disabled']
    json_box['state'] = ['normal']
    json_box.delete(1.0, 'end')
    json_box['state'] = ['disabled']
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
# useful for when the user is in their next game and wants to change game title/char without backspacing everything
def clear_entries():
    gameEntry.delete(0, 'end')
    characterEntry.delete(0, 'end')


# render window with tkinter
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
frm_json = tk.Frame()
frm_json.pack(fill=tk.X, ipadx=5, ipady=5)
json_box = tk.Text(master=frm_json, width=50, height=5)
json_box.pack()
json_box['state'] = ['disabled']

# frame for copy to clipboard button
frm_copy = tk.Frame()
frm_copy.pack(fill=tk.X, ipadx=5, ipady=5)

# copy to clipboard button
btn_copy = tk.Button(master=frm_copy, text="Copy data to clipboard", command=copy_json)
btn_copy.pack(side=tk.LEFT, padx=10, ipadx=10)

# Start the application
window.mainloop()
