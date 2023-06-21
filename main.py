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


def continueprcs():
    print(Fore.BLUE + "Connecting To Serial Port...")
    try:
        ser = serial.Serial(comport, baudrate)
    except KeyboardInterrupt:
        print(Fore.RED + "Something Has Gone Really Wrong! Check Details Please!\nClosing Program...")
        sys.exit(2)
    print(Fore.GREEN + "Connected To Serial Port!" + Style.RESET_ALL)

    tosendorrecv = input(Fore.BLUE + "Do You Want To Send or Receive Data? (s/r): ")
    if str(tosendorrecv.lower()) == "s":
        datatobesent = input(Fore.BLUE + "What Do You Want To Send?: ")
        if len(str(datatobesent)) == 0:
            print(Fore.RED + "Data Can't Be Empty!" + Style.RESET_ALL)
            exit(1)
    elif str(tosendorrecv.lower()) == "":
        print(Fore.GREEN + "Received Data: " + str(ser.readline()))


# Check if arguments are missing
if len(sys.argv) != 3:
    print(Fore.RED + "Usage: python script.py <COM Port> <Baud Rate>" + Style.RESET_ALL)
    sys.exit(1)

# Get the arguments
comport = sys.argv[1]
baudrate = sys.argv[2]

# Check if any argument is empty
if not comport or not baudrate:
    print(Fore.RED + "Error: Both arguments are required.\nUsage: python script.py <COM Port> <Baud Rate>")
    sys.exit(1)

# Use the arguments
print(Fore.GREEN + "COM PORT Given: " + comport)
print(Fore.GREEN + "BAUD RATE Given: " + baudrate)

ynconfirm = input(Fore.BLUE + "Is This Info Correct? (y/n): ")
if str(ynconfirm.lower()) == "y":
    continueprcs()
elif str(ynconfirm.lower()) == "n":
    print(Fore.RED + "Closing...")
    sys.exit(1)
