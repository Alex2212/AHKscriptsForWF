import ctypes
from logging import error
from multiprocessing import Process, Value, Array
from time import sleep
import pyautogui as ahk
from sqlalchemy import true
import pydirectinput as di
import sys
import random
from ctypes import *
import win32.lib.win32con as win32con

user32 = windll.user32
kernel32 = windll.kernel32
ahk.FAILSAFE = True


def cast(
    sw, cooldown=0.5, key="1",
):

    while True:

        if cooldown != -1 and sw.value == True:
            rand = random.randrange(150, 250) / 1000
            di.keyDown(key)
            sleep(rand)
            di.keyUp(key)
            sleep(cooldown - rand)
        else:
            print(f"cast: {sw.value}")
            sleep(1)


def attack(sw):
    try:
        while True:
            x, y = ahk.position()
            positionStr = "X: " + str(x).rjust(10) + " Y: " + str(y).rjust(10)
            key_state = user32.GetKeyState(win32con.VK_END)
            print(positionStr + " " + str(key_state), end="")
            print("\b" * len(positionStr + " " + str(key_state)), end="", flush=True)
    except KeyboardInterrupt:
        print("\n")


def listenEnd(sw):

    while True:
        if user32.GetKeyState(win32con.VK_END) & 0x8000:
            sw.value = not sw.value
            print(f"Listen {sw.value}")
            sleep(1)


if __name__ == "__main__":

    sw = Value(ctypes.c_bool, True)

    proc0 = Process(target=listenEnd, args=(sw,))
    proc1 = Process(target=cast, args=(sw, 1, "1"))
    proc5 = Process(target=attack, args=(sw,))

    proc0.start()
    proc1.start()

