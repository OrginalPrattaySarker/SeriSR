import time
import serial
import sys
import colorama
from colorama import Fore, Back, Style


def continueprcs():
    print("Connecting To Serial Port...")
    try:
        ser = serial.Serial(comport, baudrate)
    except:
        print(Fore.RED + "Something Has Gone Really Wrong! Check Details Please!\nClosing Program...")
        time.sleep(2)
        sys.exit(2)
    print(Fore.GREEN + "Connected To Serial Port!")

    tosendorrecv = input("Do You Want To Send or Receive Data? (s/r): ")
    if str(tosendorrecv.lower()) == "s":
        datatobesent = input("What Do You Want To Send?: ")
        if len(str(datatobesent)) == 0:
            print("Data Can't Be Empty!")

    elif str(tosendorrecv.lower()) == "":
        print("Received Data: " + str(ser.readline()))


# Check if arguments are missing
if len(sys.argv) != 3:
    print("Usage: python script.py <COM Port> <Baud Rate>")
    sys.exit(1)

# Get the arguments
comport = sys.argv[1]
baudrate = sys.argv[2]

# Check if any argument is empty
if not comport or not baudrate:
    print("Error: Both arguments are required.")
    print("Usage: python script.py <COM Port> <Baud Rate>")
    sys.exit(1)

# Use the arguments
print("COM PORT Given: " + comport)
print("BAUD RATE Given: " + baudrate)

ynconfirm = input("Is This Info Correct? (y/n): ")
if str(ynconfirm.lower()) == "y":
    continueprcs()
elif str(ynconfirm.lower()) == "n":
    sys.exit(1)