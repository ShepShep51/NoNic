import tkinter as tk
from tkinter import ttk
import datetime
from time import sleep

normfont = ('Helvetica', 12)

def timeReturn():
    timestamp = datetime.datetime.now().time()
    return timestamp

def PopUpStart():
    popup = tk.Tk()
    popup.wm_title('!')
    label = ttk.Label(popup, text='You can start', font=normfont)
    label.pack(side="top", fill='x', pady=10)
    B1 = ttk.Button(popup, text='Okay', command =lambda:[popup.destroy(),timeReturn()])
    B1.pack(side=tk.LEFT)
    popup.mainloop()
    return timeReturn()

def PopUpEnd():
    popup = tk.Tk()
    popup.wm_title('!')
    label = ttk.Label(popup, text='You need to stop now', font=normfont)
    label.pack(side="top", fill='x', pady=10)
    B1 = ttk.Button(popup, text='Stopped', command=lambda:[popup.destroy(),timeReturn()])
    B1.pack(side=tk.LEFT)
    popup.mainloop()
    return timeReturn()

def popCycle(on, off):
    while True:
        PopUpStart()
        onTime = on * 60
        sleep(onTime)
        PopUpEnd()
        offTime = off * 60
        sleep(offTime)

def Timer():
    standin = datetime.date(1,1,1)
    minOn = 30
    minOff = 60
    startTime = datetime.time(7,30,0)
    endTime = datetime.time(22,30,0)
    minShift = datetime.timedelta(minutes=5)
    d1 = datetime.date(2020,9,21)
    d2 = datetime.date.today()
    comb = datetime.datetime.combine(standin,startTime).time()
    combEnd = datetime.datetime.combine(standin,endTime).time()
    while True:
        if d1 != d2:
            d1 = datetime.date.today()
            minOff = minOff + 5
            startTime = (datetime.datetime.combine(datetime.date(1,1,1),startTime)+minShift).time()
            endTime = (datetime.datetime.combine(datetime.date(1,1,1),endTime)-minShift).time()
        else:
            while datetime.datetime.now().time() >= comb and datetime.datetime.now().time() <= combEnd:
             popCycle(minOn,minOff)
            else:
                PopUpEnd()

Timer()