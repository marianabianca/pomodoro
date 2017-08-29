import time
import os

print ("Pomodoro started")

time_to_work = 60 * 25  # 60 - seconds in 1 minute | 25 - minutes to work
time_to_rest = 60 * 5 # 60 - seconds in 1 minute | 5 - minutes to rest
end_of_pomodoro = 60 * 30 # 60 - seconds in 1 minute | 30 - minutes to rest

new_pomodoro = True;

while (new_pomodoro):
	for i in range(0, 3):
		time.sleep(time_to_work);
		os.system("gnome-terminal -e 'bash -c \"python print_rest.py; exec bash\"'")
		time.sleep(time_to_rest);
		os.system("gnome-terminal -e 'bash -c \"python print_work.py; exec bash\"'")

	time.sleep(time_to_work);
	os.system("gnome-terminal -e 'bash -c \"python print_rest.py; exec bash\"'")
	time.sleep(end_of_pomodoro);
	os.system("gnome-terminal -e 'bash -c \"python print_work.py; exec bash\"'")
	
	new_pomodoro = raw_input("Do you want to start a new pomodoro? (y/n) ")
	
	if new_pomodoro == "y":
		new_pomodoro = True;
	else:
		new_pomodoro = False;
