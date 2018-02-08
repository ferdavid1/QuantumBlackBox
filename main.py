import serial
from numpy.random import choice
import os
#try:
serialArduino = serial.Serial('/dev/ttyACM0', 115200) # open serial connection to Arduino
#except serial.serialutil.SerialException:
	#os.system("arduino") # in case 
print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

def emulate_quantum_choice(angle):
    
    # this function returns -1 or 1 with probability = parameter 'probability'
    # for example, the angle 90 degrees returned the probability 50% that it was -1 or 1
    # then this function would make a 50/50 choice between -1 or 1
    angle = abs(int(angle))
    thetas = list(range(0, 181))
    
    probabilities = [0.00555*x for x in range(181)] #1/180 = 0.00555, range is 180+1
    # this works! for example, probabilities[90] returns 0.4995, or 0.5, or 50%

    draw = choice([1, -1], 1, p=[probabilities[angle], 1-probabilities[angle]]) # probability of 1 is .50, probability of -1 is 1-0.50 = 0.50
    # choice(list_of_candidates, number_of_items_to_pick, p=probability_distribution)
    return int(draw)

def draw_qubit():
    
    from turtle import write, undo, delay, pensize, penup, pendown, pencolor, pos, setpos, goto, forward, left, right, backward, mainloop
    setpos(0,0)
    
    for x in range(42):
        left(15)
        forward(10)

    def dotted_line(hash_length, line_length): # like this --------- at any angle

        for x in range(line_length):
            
            forward(hash_length)
            penup()
            forward(hash_length*1.5) # length of space between hashes is (length of the hash * 1.50)
            pendown()
            forward(hash_length)

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
    # point is 35.30 degrees from origin

    penup()
    setpos(-650, 200)
    pensize(10)
    pencolor("Blue")

    write("-------------------------\n\nThe particle's angle from origin is -35.30 degrees.\n\nWhen the gyroscope is aligned at this angle with the particle, likelihood of encountering the particle in that state will read 1.\n\nThe more out of alignment the gyroscope is with the qubit's yaw, the more random the likelihood of that state is.\n\nWhen the gyroscope is orthogonal to the qubit angle of yaw, likelihood of that state is completely random\n\nNote: 'randomness' is evaluated according to a quantum probability amplitude value.\n\n-------------------------")
    setpos(-200, 100)
    for i in range(4000):
        while (serialArduino.inWaiting()==0):
            serialArduino.write(b'a') # send arduino a serial pulse

        try:
            valueRead = serialArduino.readline(50) #500
            valueInInt = float(valueRead)
            print(valueInInt)
            write("Probability: \n")
            if valueInInt < 36 and valueInInt > 34: # spin angle is about 35.3
                write(int(1))
                undo()
                delay(1000)

            elif valueInInt < -144 and valueInInt > -146: #this is the negative of the spin angle,  180-35.3 = 145
                write(int(-1))
                undo()
                delay(1000)
            else:
                decision = emulate_quantum_choice(valueInInt)
                # print(decision)
                write(decision)
                undo()
                delay(1000)

        except ValueError:
            pass  

    mainloop()

if __name__ == '__main__':

    def testing_quantum_choice(angle):
        rec = []
        for x in range(100):
            rec.append(emulate_quantum_choice(angle))
        print(rec.count(1), rec.count(-1)) # verify the choice is 'random' according to the relevant angle probability

    draw_qubit()
    