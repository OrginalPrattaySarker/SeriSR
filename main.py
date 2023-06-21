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
        sys.exit(0)
    except serial.SerialException:
        print(Fore.RED + "Details Are Wrong, Please Check!" + Style.RESET_ALL)
    except:
        print(Fore.RED + "Something Has Gone Really Wrong!\nClosing Program..." + Style.RESET_ALL)
        sys.exit(2)
    print(Fore.GREEN + "Connected To Serial Port!" + Style.RESET_ALL)
    datatobesent = input(Fore.BLUE + "What Do You Want To Send?: ")
    if len(str(datatobesent)) == 0:
        print(Fore.RED + "Data Can't Be Empty!" + Style.RESET_ALL)
        exit(1)


# Check if arguments are missing
if len(sys.argv) != 3:
    print(Fore.RED + "Usage: python script.py <COM Port> <Baud Rate>" + Style.RESET_ALL)
    sys.exit(1)

# Get the arguments
comport = sys.argv[1]
baudrate = sys.argv[2]

# Check if any argument is empty
if not comport or not baudrate:
    print(Fore.RED + "Error: Both arguments are required.\nUsage: python script.py <COM Port> <Baud Rate>" + Style.RESET_ALL)
    sys.exit(1)

# Use the arguments
print(Fore.GREEN + "COM PORT Given: " + comport)
print(Fore.GREEN + "BAUD RATE Given: " + baudrate)
print(Fore.GREEN + "Trying To To Serial Port...")
try:
    ser = serial.Serial(comport, baudrate)
except KeyboardInterrupt:
    sys.exit(0)
except serial.SerialException:
    print(Fore.RED + "Details Are Wrong, Please Check!" + Style.RESET_ALL)
except:
    print(Fore.RED + "Something Has Gone Really Wrong!\nClosing Program..." + Style.RESET_ALL)
    sys.exit(2)
print(Fore.GREEN + "Connected To Serial Port!" + Style.RESET_ALL)
datatobesent = input(Fore.BLUE + "What Do You Want To Send?: ")
if len(str(datatobesent)) == 0:
    print(Fore.RED + "Data Can't Be Empty!" + Style.RESET_ALL)
    exit(1)
