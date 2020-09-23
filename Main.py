import tkinter as tk
from tkinter import ttk
import datetime
from time import sleep

normfont = ('Helvetica', 12)

def timeReturn():
    #Made this function so that it can be called when a notification button is pressed
    #It allows for a timestamp to be logged
    timestamp = datetime.datetime.now().time()
    return timestamp

def PopUpStart():
    #Notification function to start a timer
    popup = tk.Tk()
    popup.wm_title('!')
    label = ttk.Label(popup, text='You can start', font=normfont)
    label.pack(side="top", fill='x', pady=10)
    B1 = ttk.Button(popup, text='Okay', command =lambda:[popup.destroy(),timeReturn()])
    B1.pack(side=tk.LEFT)
    popup.mainloop()
    return timeReturn()

def PopUpEnd():
    #Notification function to end a timer
    popup = tk.Tk()
    popup.wm_title('!')
    label = ttk.Label(popup, text='You need to stop now', font=normfont)
    label.pack(side="top", fill='x', pady=10)
    B1 = ttk.Button(popup, text='Stopped', command=lambda:[popup.destroy(),timeReturn()])
    B1.pack(side=tk.LEFT)
    popup.mainloop()
    return timeReturn()

def popCycle(on, off, startTime, endTime):
    ### A function to continuously call the start/stop functions, with pauses inbetween
    #Changed from while True because once called it would not stop even if it was outside run times
    while datetime.datetime.now().time() > startTime and datetime.datetime.now().time() < endTime:
        PopUpStart()
        onTime = on * 60
        sleep(onTime)
        PopUpEnd()
        offTime = off.seconds
        sleep(offTime)

def dateCheck(start,minOff,minInc,startTime,endTime):
    sDate = datetime.datetime.strptime(start, '%m/%d/%y')
    cDate = datetime.datetime.now().date()
    dateDiff = cDate - sDate.date()
    minShift =  datetime.timedelta(minutes=minInc) * dateDiff.days
    minutesOff = datetime.timedelta(minutes=minOff)

    minutesOff = minutesOff + minShift
    startTime = (datetime.datetime.combine(datetime.date(1,1,1),startTime)+minShift).time()
    endTime = (datetime.datetime.combine(datetime.date(1,1,1),endTime)-minShift).time()
    return (minutesOff,startTime,endTime)

#TODO: Write a main menue GUI that shows start time and end time, shows %decrease in time overall,
# total money saved, some bar graphs?, timestamps of the previous day, and an insperational message?

def Timer():
    minOn = 30 #starting number of minutes on
    minOff = 60 #starting number of minutes off
    startTime = datetime.time(7,30,0) #starting time for when program can start
    endTime = datetime.time(22,30,0) #starting time for when program should end
    minShift = datetime.timedelta(minutes=5) #incriment that start/stop should be increased/decreased respectively
    d1 = datetime.date(2020,9,21) #initialized date comparison
    d2 = datetime.date.today() #comparison for d1
    minOff, startTime, endTime = dateCheck('9/21/20',minOff,5,startTime,endTime)
    while True:
        if datetime.datetime.now().time() < startTime:
         sleep(60)
        elif datetime.datetime.now().time() > endTime:
            break
        else:
            popCycle(minOn,minOff,startTime,endTime)


Timer()