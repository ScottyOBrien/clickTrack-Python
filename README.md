# clickTrack.py
python script to track clicks 

You will need the latest version of python installed to run this script: https://www.python.org/
  - Make sure when you run the installer you choose the option to **add Python to the PATH file**

### Who clicks more?

My girlfriend and I had a dispute over who clicks more on a given day. I started this project as an effort to prove her wrong!
  - This script will keep track of left and right clicks, to finish execution  do shift+a+x (might change this eventually, for now it works)
  - it will print the total amount of clicks, left clicks, and right clicks in a log file that will be created in the directory where the script is run
  - If you are on windows I recommend setting up a bat file to run the script to make the process a bit faster
  
Here is an example of what your bat file might look like:

```
@echo off
py C:\change this to where ever you put\clickTrack.py
pause
```
  - to create this, right click somewhere in a folder or on your desktop and create new text document.
  - copy and paste the above code, file save-as "filename-whatever".bat

## How to run this script (on windows)
  1. Make sure you have Python installed, and added to your PATH
  2. Open cmd type ```pip install pynput``` and press enter
  3. Create your bat file using the example above, I recommend creating a new folder somewhere on your PC for this
  4. double click the bat file, fill out the prompts, follow onscreen instructions :)
  5. **remember**: You must do shift+a+x to save your clicks to the log file, if you close before this your **clicks will be lost!**
