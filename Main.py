from Tkinter import *
from threading import Thread
import time
from scenario import *
import win32api, win32con
from consts import *
import random as rnd

root = Tk()
root.geometry('+{0}+{1}'.format(WINDOW_START_POSITION[0], WINDOW_START_POSITION[1]))

titleE = Label(root, text="MishanyaAI")
titleE.pack()

is_started = False
main_thr = Thread()


def go():
    global is_started
    i = 0
    while is_started:
        print(i)
        main_scenario()
        i += 1
        break
    print "Finished"


def start():
    global main_thr, is_started
    if is_started:
        print("Already started")
    else:
        print "Start"
        is_started = True
        track_thr = Thread(target=motion)
        track_thr.start()
        main_thr = Thread(target=go)
        main_thr.start()


def stop():
    global is_started
    is_started = False


def foo():
    define_context()


startB = Button(root, text="Start", command=start, width=15, height=5)
startB.pack()
stopB = Button(root, text="Stop", command=stop, width=15, height=5)
stopB.pack()
testB = Button(root, text="Test", command=foo, width=15, height=5)
testB.pack()
input1 = Entry(root)
input1.pack()
input2 = Entry(root)
input2.pack()


def motion():
    global is_started
    while is_started:
        time.sleep(0.01)
        x, y = win32api.GetCursorPos()
        mouse1.delete(0, END)
        mouse1.insert(0, x)
        mouse2.delete(0, END)
        mouse2.insert(0, y)


mouse1 = Entry(root)
mouse1.pack()
mouse2 = Entry(root)
mouse2.pack()

root.mainloop()
