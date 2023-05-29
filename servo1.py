from tkinter import *
from pyfirmata import Arduino, util
import time

board = Arduino('COM3')
it = util.Iterator(board)
it.start()
servo = board.get_pin('d:9:s')

screen = Tk()
screen.geometry("400x500")
var = DoubleVar()
isSweep = False

def servo_handler(angle):
    if not isSweep :
        print(angle)
        servo.write(angle)

def sweep():
    servo_angle = 0
    for angle in range(180):
        servo_angle =  angle
        servo.write(servo_angle)
        time.sleep(0.1)
    isSweep = False

button_Ok = Button(screen, text="Putar", command=sweep)
button_Ok.pack(anchor=CENTER)
w = Scale(screen, variable=var, orient=HORIZONTAL, from_=0, to=180)
w.pack(anchor=CENTER)

screen.mainloop()