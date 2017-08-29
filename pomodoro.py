import time
import os

def minutes_to_seconds(minutes):
	"""
	A function that converts minutes to seconds
	
	:param minutes: The number of minutes do be converted
	:return: The number of seconds in a give number of minutes
	"""
	return 60 * minutes

print ("Pomodoro started")

time_to_work = minutes_to_seconds(25)
time_to_rest = minutes_to_seconds(5)
end_of_pomodoro = minutes_to_seconds(30)

new_pomodoro = True;

while (new_pomodoro):
	for i in range(0, 3):
		time.sleep(time_to_work);
		os.system("x-terminal-emulator -e 'bash -c \"python print_rest.py; exec bash\"'")
		time.sleep(time_to_rest);
		os.system("x-terminal-emulator -e 'bash -c \"python print_work.py; exec bash\"'")

	time.sleep(time_to_work);
	os.system("x-terminal-emulator -e 'bash -c \"python print_rest.py; exec bash\"'")
	time.sleep(end_of_pomodoro);
	os.system("x-terminal-emulator -e 'bash -c \"python print_work.py; exec bash\"'")
	
	new_pomodoro = raw_input("Do you want to start a new pomodoro? (y/n) ")
	
	if new_pomodoro == "y":
		new_pomodoro = True;
	else:
		new_pomodoro = False;
