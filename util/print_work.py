# coding: utf-8

import os
import sys
import time

print("")
print("")
print("")
print("")
print("")
print(".¸¸.*♡*.¸¸.*☆*¸.*♡*.¸¸.*☆*.¸¸.*♡*.¸¸.*☆*")
print("")

print("                Time to work            ")

print("")
print(".¸¸.*♡*.¸¸.*☆*¸.*♡*.¸¸.*☆*.¸¸.*♡*.¸¸.*☆*")
print("")
print("")
print("")
print("")
print("")

time.sleep(int(sys.argv[1]))
if (os.name == 'nt'):
    os.kill(os.getpid(), 9)
else:
    os.kill(os.getppid(), 9)
