#!/usr/bin/env python
#coding=utf-8
#http://framboise-pi.fr


import Tkinter as tk
from Tkinter import *
import time
from time import sleep
from datetime import datetime, timedelta
import os
import MPMM_config
import MPMM_sensehat
import ttk
import MPMM_module_words

clock_time_temporary = ''
sensehat_temporary = 0
sensehat_temporary_result = 0

# Loading dialog window
welcome_window = tk.Tk()
welcome_window.title('Loading')
welcome_window.configure(background='black')
welcome_window.overrideredirect(True)
welcome_window.columnconfigure(0, weight=1)
welcome_window.rowconfigure(0, weight=1)
welcome_window.rowconfigure(1, weight=1)

welcome_text = tk.Label(welcome_window, font = MPMM_config.welcomefont, bg='black', fg='white')
welcome_text.config(text=MPMM_config.welcome)
welcome_text.grid(column=0,row=0)

# Progression Bar with style
style = ttk.Style()
style.theme_use('default')
style.configure("red.Horizontal.TProgressbar", background='red')
bar = ttk.Progressbar(welcome_window, length=200, style='red.Horizontal.TProgressbar')
bar['value'] = 0
bar.grid(column=0, columnspan=2, row=1)

vertical = welcome_window.winfo_reqheight()
vertical_milieu = int(welcome_window.winfo_screenheight()/2)
welcome_window.geometry(str(welcome_window.winfo_screenwidth()) + "x" + str(vertical) + "+0+" + str(vertical_milieu))
welcome_window.update()

bar['value'] = 25
welcome_window.update()

#Sensehat display welcome
if MPMM_config.sensehat_on:
        MPMM_sensehat.Welcome()

# Prog Bar animation
bar['value'] = 50
welcome_window.update()
time.sleep(0.5)
bar['value'] = 75
welcome_window.update()
time.sleep(0.5)
bar['value'] = 100
welcome_window.update()

welcome_window.destroy()
if (MPMM_config.sensehat_on):
    MPMM_sensehat.Blank()

fullwindow = tk.Tk()
fullwindow.title('MPMM')
fullwindow.attributes("-fullscreen", True)
fullwindow.configure(background='black')
fullwindow.columnconfigure((0,1,2,3), weight=1)
fullwindow.columnconfigure(4, weight=10)
fullwindow.rowconfigure(0, weight=1)
fullwindow.rowconfigure(1, weight=2)
fullwindow.rowconfigure((2,3,4,5), weight=20)

## ROW 0
date_display = tk.Label(fullwindow, font = MPMM_config.font_date, bg='black', fg='white')
date_display.grid(column=1, row=0, columnspan = 6, ipadx=2, ipady=2, sticky=SW)
## ROW 1
clock_hour_display = tk.Label(fullwindow, font = MPMM_config.font_hour, bg='black', fg='white')
clock_hour_display.grid(column=1, row=1, sticky=NE)
#
clock_time_minutes_display = tk.Label(fullwindow, font = MPMM_config.font_minutes, bg='black', fg='white')
clock_time_minutes_display.grid(column=3, row=1, sticky=NW)
#
clock_seconds_display = tk.Label(fullwindow, font = MPMM_config.font_secondes, bg='black', fg='white')
clock_seconds_display.grid(column=2, row=1)
## ROW 3

## ROW 4

## ROW 5 ## FOOTER
module_words_display = tk.Message(fullwindow, font = MPMM_module_words.module_words_font, bg='black', fg='white')
module_words_display.grid(column=0, row=5, columnspan=6,  ipadx=10, ipady=10)
module_words_display_width = fullwindow.winfo_screenwidth() - (fullwindow.winfo_screenwidth()/6)

def ClockTime():
    global clock_time_temporary
    global sensehat_temporary
    global sensehat_temporary_result
    clock_time = time.strftime("%H")
    if clock_time != clock_time_temporary:
        clock_time_temporary = clock_time
        clock_hour_display.config(text=clock_time)
    if MPMM_config.sensehat_on:
        if sensehat_temporary == (MPMM_sensehat.blank*2):
            MPMM_sensehat.Randomize()
        if sensehat_temporary == (MPMM_sensehat.blank*2 + MPMM_sensehat.display*2):
            MPMM_sensehat.Blank()
            sensehat_temporary = 0
        else:
            sensehat_temporary = sensehat_temporary + 1

    clock_hour_display.after(500, ClockTime)

def ClockTimeMinutes():
    clock_time_minutes = time.strftime("%M")
    clock_time_minutes_display.config(text=clock_time_minutes)
    clock_time_minutes_display.after(500, ClockTimeMinutes)

def ClockTimeSeconds():
    clock_time_seconds = time.strftime(":%S:")
    clock_seconds_display.config(text=clock_time_seconds)
    clock_seconds_display.after(500, ClockTimeSeconds)
            
def ClockDate():
    day = MPMM_config.days[time.localtime()[6]]
    month = MPMM_config.months[time.localtime()[1]-1]
    clock_date = day + " " +  time.strftime("%d") + " " + month
    date_display.config(text=clock_date)
    date_display.after(500, ClockDate)

def Module_Messages():
    module_words_output=MPMM_module_words.RandomWords()
    module_words_display.config(text=module_words_output, anchor=CENTER, justify=CENTER, width=fullwindow.winfo_screenwidth())
    module_words_display.after(MPMM_module_words.interval, Module_Messages)

################################

def leave(event):
    if MPMM_config.sensehat_on:
        MPMM_sensehat.Blank()
    fullwindow.destroy()
    sys.exit()
fullwindow.bind('<Escape>',leave)
    
#########################

ClockDate()
ClockTime()
ClockTimeMinutes()
ClockTimeSeconds()
if MPMM_config.module_words_on:
    Module_Messages()

########################


# TKINTER mainloop blocking 
fullwindow.mainloop()
#fullwindow.update_idletasks()
#fullwindow.update()
