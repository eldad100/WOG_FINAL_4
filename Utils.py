import os
import time

SCORES_FILE_NAME = 'Scores/Scores.txt'

BAD_RETURN_CODE = "Error code 200"

def Screen_cleaner():
    time.sleep(0.7)
    if os.name == 'nt':  # Check if the OS is Windows
        os.system('cls')  # Clear the screen using "cls" command
    else:  # if the if block its not returning True then it will use it for linux
        os.system('clear')  # Clear the screen using "clear" command




