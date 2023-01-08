import imp
import tkinter as tk
from tkinter import *
import random
import time
from turtle import back, color
from xml.etree.ElementTree import tostring
root = Tk();
root.title("Pseudo-Randomness!")
# root.geometry('800x500')

canvas = tk.Canvas(root, width=800, height=500, background='black')
canvas.pack()
def colors(List):
    colorPicker = random.randint(0, len(List) - 1)
    return List[colorPicker]
def randomize():
    start_time = time.time()
    canvas.delete('all')
    # random.seed(5)
    for x in range(0, 200):
        for y in range(0, 100):
            
            x = random.randint(0, 801)
            y = random.randint(0, 501)
            # time.sleep(0.01)
            canvas.create_line(x, y, x+1, y, width= 0.5, fill= colors(['white']))
    end_time = time.time();
    total_time = end_time - start_time
    total_time = round(total_time, 4)
    lb = Label(text="Time:" + str(total_time), ).place(x= 100, y=505)

            
button = tk.Button(text="Generate", command=randomize, background= 'white')
button.pack()
root.update()
root.mainloop()


