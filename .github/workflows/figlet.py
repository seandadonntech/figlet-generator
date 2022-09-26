import pyfiglet
# made by seandadonntech , technio#7716, aka lilcryptotech
from colorama import Fore, Back, Style
print(Fore.GREEN + 'A  program that genrates text into pyfiglet  made by seandadonntech , technio#7716, ')
direction = input("what options of text do you to print? options available are slant\n")
if direction == "slant": # this is an argument/ IM ADDING MORE OPTIONS FOR THIS PROGRAM
 input = input("what text to you what to print out?\n")
result = pyfiglet.figlet_format(f"{input}", font = "slant" )


print(result)
