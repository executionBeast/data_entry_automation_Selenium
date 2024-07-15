import random
import keyboard as kb
import pyautogui as pg
from time import sleep
i=0
while i<14:
    if kb.is_pressed("q"):
        sleep(1)
        print(pg.position())
        i+=1


