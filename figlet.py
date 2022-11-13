

# made by seandadonntech , technio#7716, aka lilcryptotech
from time import *

import pyfiglet
from colorama import Back, Fore, Style

print(Fore.GREEN + 'A  program that genrates text into pyfiglet  made by seandadonntech , technio#7716, Copyright (c) 2022, lilcryptotech All rights reserved. ')



direction = input("what options of text do you to print? don't know type help for list of commands \n")
#----------------------------------------------
#slant mode
#------------------------------------------------------------------------------------------------------------------------
if direction == "slant": # this is an argument/ IM ADDING MORE OPTIONS FOR THIS PROGRAM
  input = input("what text to you what to print out in slant mode?\n")
result = pyfiglet.figlet_format(f"{input}", font = "slant" )
print(result)
#---------------------------------------------------------------
if direction == "3-d":
  input = input("What text do you want to print out in 3-d mode?\n")
result = pyfiglet.figlet_format(f"{input}", font = "3-d")
print(result)

if direction == "doh":
 input = input("What text to you want to print out in doh mode?")
result = pyfiglet.figlet_format(f"{input}", font = "doh")
print(result)

if direction =="thin":
 input = input("What text you want to print thin mode")
 result = pyfiglet.figlet_format(f"{input}", font = "thin")
print(result)

if direction == "3d-banner":
 input = input("What text do you want to in banner3-D")
 result = pyfiglet.figlet_format(f"{input}", font = "banner3-D")
print(result)
print(f"you choose {direction} mode")



