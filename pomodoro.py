import time
import os
from sys import platform as _platform
import platform


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

def work(time_to_work=TIME_TO_WORK):
    _open_terminal("print_work.py", time_to_work)
    time.sleep(time_to_work)


def rest(time_to_rest=TIME_TO_REST):
    _open_terminal("print_rest.py", time_to_rest)
    time.sleep(time_to_rest)


if __name__ == '__main__':
    print("Pomodoro started")

    while (True):
        for i in range(3):
            work()
            rest()
        work()
        rest(END_OF_POMODORO)

        new_pomodoro = raw_input("Do you want to start a new pomodoro? (y/n) ")
        if new_pomodoro.lower() != "y":
            break
