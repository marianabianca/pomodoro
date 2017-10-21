import time
import os
from sys import platform as _platform

def minutes_to_seconds(minutes):
	"""
	A function that converts minutes to seconds
	
	:param minutes: The number of minutes do be converted
	:return: The number of seconds in a give number of minutes
	"""
	return 60 * minutes


TIME_TO_WORK = minutes_to_seconds(25)
TIME_TO_REST = minutes_to_seconds(5)
END_OF_POMODORO = minutes_to_seconds(30)


def open_terminal(python_script, time_to_close=5):
        """Open a new terminal with the python script passed

        :param python_script: The path of the python script to be
        executed
        :param time_to_close: the number of seconds before closing
        the new terminal
        """
        if _platform == "darwin":  #macOS
            os.system("xterm -e 'bash -c \"python %s  %d; exec bash\"'" % (python_script, time_to_close))
        else:
            os.system("x-terminal-emulator -e 'bash -c \"python %s  %d; exec bash\"'" % (python_script, time_to_close))


def work(time_to_work=TIME_TO_WORK):
    open_terminal("print_work.py", time_to_work);
    time.sleep(time_to_work);


def rest(time_to_rest=TIME_TO_REST):
    open_terminal("print_rest.py", time_to_rest)
    time.sleep(time_to_rest)


print ("Pomodoro started")

new_pomodoro = True;
while (new_pomodoro):
    for i in range(0, 3):
        work()
        rest()
    work()
    rest(END_OF_POMODORO)

    new_pomodoro = raw_input("Do you want to start a new pomodoro? (y/n) ")
    if new_pomodoro == "y":
        new_pomodoro = True;
    else:
        new_pomodoro = False;
