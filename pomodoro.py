# coding: utf-8

import time
import os
import platform

from sys import platform as _platform

try:
	print "",
	python_version = 2
except:
	python_version = 3

START_MESSAGE = "Pomodoro started..."
NOTIFICATION_TIME_TO_WORK = """.¸¸.*♡*.¸¸.*☆*¸.*♡*.¸¸.*☆*.¸¸.*♡*.¸¸.*☆*
\n            Time to work\n\n.¸¸.*♡*.¸¸.*☆*¸.*♡*.¸¸.*☆*.¸¸.*♡*.¸¸.*☆*"""
NOTIFICATION_TIME_TO_REST = """.¸¸.*♡*.¸¸.*☆*¸.*♡*.¸¸.*☆*.¸¸.*♡*.¸¸.*☆*
\n\t\t\t   rest\n\n.¸¸.*♡*.¸¸.*☆*¸.*♡*.¸¸.*☆*.¸¸.*♡*.¸¸.*☆*"""


def minutes_to_seconds(minutes):
    """A function that converts minutes to seconds

	:param minutes: The number of minutes do be converted
	:return: The number of seconds in a give number of minutes
    """
    return 60 * minutes

def _open_terminal(python_script, time_to_close=5):
    """Open a new terminal with the python script passed

    :param python_script: The path of the python script to be
    executed
    :param time_to_close: the number of seconds before closing
    the new terminal
    """
    if _platform == "darwin":  #macOS
        os.system("xterm -e 'bash -c \"python %s  %d; exec bash\"'" %
                  (python_script, time_to_close))

    elif _platform.startswith('linux'): #linux
        if platform.linux_distribution()[0] == "arch": # Arch Linux support
            os.system(
                "xterm -e 'bash -c \"python %s  %d; exec bash\"'" %
                (python_script, time_to_close))
        else: # Debian based distros
            os.system(
                "x-terminal-emulator -e 'bash -c \"python %s  %d; exec bash\"'" %
                (python_script, time_to_close))

    elif os.name == 'nt':   #Windows
        os.system("start cmd /c python %s %d" % (python_script, time_to_close))
    else:
        os.system(
            "x-terminal-emulator -e 'bash -c \"python %s  %d; exec bash\"'" %
            (python_script, time_to_close))
        

TIME_TO_WORK = minutes_to_seconds(25)
TIME_TO_REST = minutes_to_seconds(5)
END_OF_POMODORO = minutes_to_seconds(30)


def work(time_to_work):
    _open_terminal("print_work.py", time_to_work)
    time.sleep(time_to_work)


def rest(time_to_rest):
    _open_terminal("print_rest.py", time_to_rest)
    time.sleep(time_to_rest)


def pomodoro_session(time_to_work=TIME_TO_WORK, time_to_rest=TIME_TO_REST, end_of_pomodoro=END_OF_POMODORO):
    while (True):
            for i in range(3):
                work(time_to_work)
                rest(time_to_rest)
            work(time_to_work)
            rest(END_OF_POMODORO)
			
            if python_version == 2:
				new_pomodoro = raw_input("Do you want to start a new pomodoro? (y/n) ")
            else:
				new_pomodoro = input("Do you want to start a new pomodoro? (y/n) ")
            if new_pomodoro.lower() != "y":
                break


if __name__ == '__main__':
    print(START_MESSAGE)
    time.sleep(1)

    print("Do yout want to define your own time (y/n)?")
    if python_version == 2:
		personalized_time = raw_input("Press 'n' if you want to use the default time: ")

		if personalized_time == 'y':
			print("Enter time in minutes :)")
			time_to_work = minutes_to_seconds(int(raw_input("How much time do you want to Work? ")))
			time_to_rest = minutes_to_seconds(int(raw_input("How much time do you want to Rest? ")))
			end_of_pomodoro = minutes_to_seconds(int(raw_input("How much time do you want between two pomodoro sessions? ")))
			pomodoro_session(time_to_work, time_to_rest, end_of_pomodoro)
		else:
			pomodoro_session()
    else:
        personalized_time = input("Press 'n' if you want to use the default time: ")
        if personalized_time == 'y':
			print("Enter time in minutes :)")
			time_to_work = minutes_to_seconds(int(input("How much time do you want to Work? ")))
			time_to_rest = minutes_to_seconds(int(input("How much time do you want to Rest? ")))
			end_of_pomodoro = minutes_to_seconds(int(input("How much time do you want between two pomodoro sessions? ")))
			pomodoro_session(time_to_work, time_to_rest, end_of_pomodoro)
        else:
			pomodoro_session()
