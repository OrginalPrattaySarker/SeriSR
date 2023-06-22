###########################################
#                                         #
#                                         #
# SeriSR - A CLI Project                  #
#                                         #
#            By - OpenPrattay             #
###########################################
import time
import serial
import sys
import colorama
from colorama import Fore, Back, Style

# Check if arguments are missing
if len(sys.argv) != 3:
    print(Fore.RED + Style.BRIGHT + "Usage: python script.py <COM Port> <Baud Rate>" + Style.RESET_ALL)
    sys.exit(1)

# Get the arguments
comport = sys.argv[1]
baudrate = sys.argv[2]

# Check if any argument is empty
if not comport or not baudrate:
    print(Fore.RED + Style.BRIGHT + "Error: Both arguments are required.\nUsage: python script.py <COM Port> <Baud Rate>"
          + Style.RESET_ALL)
    sys.exit(1)

# Use the arguments
print(Fore.GREEN + Style.BRIGHT + "----  SeriSR 1.0 By OpenPrattay  ----")
print(Style.RESET_ALL + "COM PORT Given: " + comport)
print(Style.RESET_ALL + "BAUD RATE Given: " + baudrate)
print(Fore.GREEN + Style.BRIGHT + "Trying To Connect To Serial Port...")
try:
    ser = serial.Serial(comport, baudrate)
except KeyboardInterrupt:
    sys.exit(0)
except serial.SerialException:
    print(Fore.RED + Style.BRIGHT + "Details Are Wrong, Please Check!" + Style.RESET_ALL)
    sys.exit()
except:
    print(Fore.RED + Style.BRIGHT + "Something Has Gone Really Wrong!\nClosing Program..." + Style.RESET_ALL)
    sys.exit(2)
print(Fore.GREEN + Style.BRIGHT + "Connected To Serial Port!" + Style.RESET_ALL)
datatobesent = input("What Do You Want To Send?: ")
if len(str(datatobesent)) == 0:
    print(Fore.RED + Style.BRIGHT + "Data Can't Be Empty!" + Style.RESET_ALL)
    exit(1)
