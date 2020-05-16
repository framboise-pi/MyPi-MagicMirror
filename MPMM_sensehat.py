#!/usr/bin/env python
#coding=utf-8
#http://framboise-pi.fr

from sense_hat import SenseHat
from sensehat_pictures import *
import MPMM_config
import random
from random import randint

sense = SenseHat()
sense.rotation = MPMM_config.sensehat_rotation
sense.low_light = True
# seconds to display LED draw
display = 3
# seconds to leave blank between
blank = 10

def Welcome():
        sense.show_message(MPMM_config.sensehat_welcome, text_colour=[255, 0, 0])
def Blank():
        sense.clear()
def Randomize():
        dice = random.randint(0,5)
        if dice == 0:
                sense.set_pixels(monstre_01);
        if dice == 1:
                sense.set_pixels(monstre_02);
        if dice == 2:
        if dice == 3:
        if dice == 4:
        if dice == 5:
