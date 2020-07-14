from pynput.keyboard import Key, Listener, Controller as KeyController
from pynput import keyboard as KB
from pynput.mouse import Button, Controller
import time
import os
import random
fCounter = 0
begTime = 0
timeCounter
keyboard = KeyController()
mouse = Controller()

time.sleep(2)
def enter(times):
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(times)
def on_release(key):
    if key == Key.esc:
        os._exit(0)

listener = KB.Listener(
    on_release=on_release)
listener.start()
while True:
    c = "pls beg pls fish pls hunt"
    for char in c:
        keyboard.press(char)
        keyboard.release(char)
        if(char == "g"):       
            enter(random.randint(10,51))
        elif (char == "h" and fCounter == 0):
            enter(random.randint(50,60))
            fCounter = 1
        elif (char == "t"):
            enter(random.randint(1, 31))
            fCounter = 0
            timeCounter += 1
        if (timeCounter == 10):
            time.sleep(240)
        time.sleep(0.06)    
