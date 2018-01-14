import serial
# import atexit
import pandas as pd
import numpy as np
import sys
import os

values = []

cnt=0

serialArduino = serial.Serial('/dev/ttyACM0', 115200) #could also be set to 115200

def doAtExit():
    serialArduino.close()
    print("Close serial")
    print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

# atexit.register(doAtExit)

print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

# set_indexes = np.arange(0, 3999, 3)

for i in range(4000):
    while (serialArduino.inWaiting()==0):
        pass
    #print("reading line...")
    valueRead = serialArduino.readline(5) #500
    # print(valueRead)
    valueInInt = float(valueRead)
    print(valueInInt)
    values.append(valueInInt) 

# for x in set_indexes:
#     print([values[x], values[x+1], values[x+2]])


#Output values to a txt file
# with open('Real_Values.txt', 'w') as data:
#     for line in values:
#         data.write(str(line) + '\n')

