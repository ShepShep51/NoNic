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

def popCycle(on, off):
    ### A function to continuously call the start/stop functions, with pauses inbetween
    while True:
        PopUpStart()
        onTime = on * 60
        sleep(onTime)
        PopUpEnd()
        offTime = off * 60
        sleep(offTime)

#TODO: Write a main menue GUI that shows start time and end time, shows %decrease in time overall,
# total money saved, some bar graphs?, timestamps of the previous day, and an insperational message?

def Timer():
    standin = datetime.date(1,1,1) #Dummy date to allow a .time object to be raised to a .datetime object
    minOn = 30 #starting number of minutes on
    minOff = 60 #starting number of minutes off
    startTime = datetime.time(7,30,0) #starting time for when program can start
    endTime = datetime.time(22,30,0) #starting time for when program should end
    minShift = datetime.timedelta(minutes=5) #incriment that start/stop should be increased/decreased respectively
    d1 = datetime.date(2020,9,21) #initialized date comparison
    d2 = datetime.date.today() #comparison for d1
    comb = datetime.datetime.combine(standin,startTime).time() #raises startTime to a .datetime object
    combEnd = datetime.datetime.combine(standin,endTime).time() #raises endTime to a .datetime object
    while True:
        if d1 != d2: #Should add a comparison between current date and 9/21/2020 showing number of days.
                     #Otherwise it will revert back to base state and never increase
            d1 = datetime.date.today()
            minOff = minOff + 5 #Increases length of break
            startTime = (datetime.datetime.combine(datetime.date(1,1,1),startTime)+minShift).time()#Makes startTime later
            endTime = (datetime.datetime.combine(datetime.date(1,1,1),endTime)-minShift).time() #Makes endTime earlier
        else:
            if datetime.datetime.now().time() < comb:
             sleep(60)
            elif datetime.datetime.now().time() > combEnd:
                break
            else:
                popCycle(minOn,minOff)


Timer()