from tkinter import *
from tkinter import ttk
import pyfirmata 

port = input("select correct port : COM3")
comport = "COM3" + port
board = pyfirmata.Arduino(comport)

root = Tk()
root.title("Firmata Arduino Controler")
root.resizable(600, 600)

led = board.get_pin('d:9:o')

def on():
    led.write(1)

def off():
    led.write(0)

ttk.Button(root,text="LED ON", width="11", command=on).grid(row=1, column=0, ipadx=1, ipady=1)
ttk.Button(root,text="LED OFF", width="11", command=off).grid(row=1, column=1, ipadx=1, ipady=1)

root.mainloop()