import pyfiglet
from colorama import Fore, Back, Style
print(Fore.GREEN + 'a  program that genrates text into pyfiglet  made by seandadonntech , technio#7716, ')
input = input("what text to you what to print out?\n")
direction = input("what options of text do you to print? options available are slant\n")
 if direction == "slant": # this is an argument/ IM ADDING MORE OPTIONS FOR THIS PROGRAM
result = pyfiglet.figlet_format(f"{input}", font = "slant"  ) # feel free to change this to whatever you want
print(result)
#THIS CODE IS OWNED BY SEANDADONNTECH 
