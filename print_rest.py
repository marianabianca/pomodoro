# coding: utf-8

import os
import sys
import time
import random

# tip messages must have 40 characters to fit the pattern below
tipMessages = ["   remember to stay properly hydrated   ",
            " take your eyes off the screen for a bit",
            "  enjoy this moment to stretch a little "]

print("")
print("")
print("")
print("")
print("")
print(".¸¸.*♡*.¸¸.*☆*¸.*♡*.¸¸.*☆*.¸¸.*♡*.¸¸.*☆*")
print("")

print("                   rest                 ")
print(random.choice(tipMessages))

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
