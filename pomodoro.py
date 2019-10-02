# coding: utf-8

import time
import os
import platform
import gi

gi.require_version('Notify', '0.7')

from gi.repository import Notify
from sys import platform as _platform


START_MESSAGE = "Pomodoro started..."
NOTIFICATION_TIME_TO_WORK = """.¸¸.*♡*.¸¸.*☆*¸.*♡*.¸¸.*☆*.¸¸.*♡*.¸¸.*☆*
\n            Time to work\n\n.¸¸.*♡*.¸¸.*☆*¸.*♡*.¸¸.*☆*.¸¸.*♡*.¸¸.*☆*"""
NOTIFICATION_TIME_TO_REST = """.¸¸.*♡*.¸¸.*☆*¸.*♡*.¸¸.*☆*.¸¸.*♡*.¸¸.*☆*
\n\t\t\t   rest\n\n.¸¸.*♡*.¸¸.*☆*¸.*♡*.¸¸.*☆*.¸¸.*♡*.¸¸.*☆*"""


Notify.init("Pomodoro")
notification = Notify.Notification.new(START_MESSAGE)


def minutes_to_seconds(minutes):
    """A function that converts minutes to seconds

	:param minutes: The number of minutes do be converted
	:return: The number of seconds in a give number of minutes
    """
    return 60 * minutes


def notify(notification_text):
    """Shows a notification conteining the text passed

    :param notification_text: The text to be displayed on the
    desktop notification
    """
    notification.clear_hints()
    notification.update(notification_text)
    notification.show()

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
    notify(NOTIFICATION_TIME_TO_WORK)
    _open_terminal("print_work.py", time_to_work)
    time.sleep(time_to_work)


def rest(time_to_rest):
    notify(NOTIFICATION_TIME_TO_REST)
    _open_terminal("print_rest.py", time_to_rest)
    time.sleep(time_to_rest)


def pomodoro_session(time_to_work=TIME_TO_WORK, time_to_rest=TIME_TO_REST, end_of_pomodoro=END_OF_POMODORO):
    while (True):
            for i in range(3):
                work(time_to_work)
                rest(time_to_rest)
            work(time_to_work)
            rest(END_OF_POMODORO)

            new_pomodoro = input("Do you want to start a new pomodoro? (y/n) ")
            if new_pomodoro.lower() != "y":
                break


if __name__ == '__main__':
    print(START_MESSAGE)
    notify(START_MESSAGE)
    time.sleep(1)

    print("Do yout want to define your own time (y/n)?")
    personalized_time = input("Press 'n' if you want to use the default time: ")

    if personalized_time == 'y':
        print("Enter time in minutes :)")
        time_to_work = minutes_to_seconds(input("How much time do you want to Work? "))
        time_to_rest = minutes_to_seconds(input("How much time do you want to Rest? "))
        end_of_pomodoro = minutes_to_seconds(input("How much time do you want between two pomodoro sessions? "))
        pomodoro_session(time_to_work, time_to_rest, end_of_pomodoro)
    else:
        pomodoro_session()
