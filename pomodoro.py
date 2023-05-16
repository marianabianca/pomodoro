# coding: utf-8

import time
import os
import sys

from win11toast import toast, notify, update_progress


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
    os.system("start cmd /c python %s %d" % (python_script, time_to_close))



TIME_TO_WORK = minutes_to_seconds(25)
TIME_TO_REST = minutes_to_seconds(5)
END_OF_POMODORO = minutes_to_seconds(30)


def work(time_to_work):
    toast('Time to work', 'Let\'s get to it', audio='ms-winsoundevent:Notification.SMS', buttons=['Dismiss'])
    time.sleep(time_to_work)


def rest(time_to_rest):
    notify(progress={
    'title': 'Short break',
    'status': 'Time to get up for a bit',
    'value': '0',
    'valueStringOverride': '0/15 videos'
    }, buttons=['Dismiss'])

    for i in range(1, time_to_rest):
        time.sleep(1)
        update_progress({'value': i/time_to_rest, 'valueStringOverride': f'{i}'/TIME_TO_REST})

    update_progress({'status': 'Completed!'})


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
    pomodoro_session()
    
    '''
    print("Do yout want to define your own time (y/n)?")
    personalized_time = input("Press 'n' if you want to use the default time: ")

    if personalized_time == 'y':
        print("Enter time in minutes :)")
        time_to_work = minutes_to_seconds(int(input("How much time do you want to Work? ")))
        time_to_rest = minutes_to_seconds(int(input("How much time do you want to Rest? ")))
        end_of_pomodoro = minutes_to_seconds(int(input("How much time do you want between two pomodoro sessions? ")))
        pomodoro_session(time_to_work, time_to_rest, end_of_pomodoro)
    else:
        pomodoro_session()
    '''
