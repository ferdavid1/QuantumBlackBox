import serial
# import atexit
import pandas as pd
import numpy as np
import sys
import os

# values = []

cnt=0

serialArduino = serial.Serial('/dev/ttyACM0', 115200) # open serial connection to Arduino

print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

if __name__ == '__main__':

    from turtle import write, pensize, penup, pendown, pencolor, pos, setpos, goto, forward, left, right, backward, mainloop
    setpos(0,0)

    def dotted_line(hash_length, line_length): # like this --------- at any angle

        for x in range(line_length):
            
            forward(hash_length)
            penup()
            forward(hash_length*1.5) # length of space between hashes is (length of the hash * 1.50)
            pendown()
            forward(hash_length)

    def quantum_random_map(angle): # map angle to some corresponding quantum probability amplitude

        

    def draw_qubit():
        
        for x in range(42):
            left(15)
            forward(10)

        left(95)
        forward(35)
        left(75)
        forward(40)
        backward(40)

        right(93)
        forward(45)
        backward(45)
        left(322)
        penup()
        forward(200)
        right(180)
        pendown()

        dotted_line(4, 30)
        # print(pos())  == (-146.56,207.00)
        # point is 39 degrees from origin

        penup()
        setpos(-800, 270)
        pensize(10)
        pencolor("Blue")

        write("-------------------------\n\nThe particle's angle from origin is -35.30 degrees.\n\nWhen the gyroscope is aligned at this angle with the particle, likelihood of encountering the particle in that state will read 1.\n\nThe more out of alignment the gyroscope is with the qubit's yaw, the more random the likelihood of that state is.\n\nWhen the gyroscope is orthogonal to the qubit angle of yaw, likelihood of that state is completely random\n\nNote: 'randomness' is evaluated according to a quantum probability amplitude value.\n\n-------------------------")
        for i in range(4000):
            while (serialArduino.inWaiting()==0):
                pass
            #print("reading line...")
            try:
                valueRead = serialArduino.readline(500) #500
                # print(valueRead)
                valueInInt = float(valueRead)
                # print(valueInInt)
                if valueInInt > -36 and valueInInt >= -35 and valueInInt < -34:
                    print(1)
                else:
                    random_value = quantum_random_map(valueInInt)
                    print(random_value)
                    # print("Something else")
                # values.append(valueInInt) 
            except ValueError:
                pass  

        mainloop()

    draw_qubit()

    