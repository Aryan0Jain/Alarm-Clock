# import required libraries
from tkinter import *
from threading import *
import datetime
import time
import winsound

# create object
root=Tk()
root.geometry("355x240")

# use threading
def Threading():
    th=Thread(target=alarm)
    th.start()

def alarm():
    # infinite loop
    while True:
        # set alarm
        alarm_time=f"{hour.get()}:{minute.get()}:{second.get()}"

        # wait for 1 second
        time.sleep(1)

        # get and print crrent time
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,alarm_time)

        # check time and play sound if its equal to alarm time
        if current_time==alarm_time:
            print("WAKE UP!!")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

# Crete UI
Label(root,text="ALARM CLOCK",font="Helvetica 0 bold",fg='red',anchor=N).grid(row=0,columnspan=6,padx=10,pady=15)
Label(root,text="CURRENT TIME",font="Helvetic 15 bold").grid(row=1,column=0,columnspan=3,padx=10)
Label(root,text="SET ALARM TIME",font="Helvetic 15 bold").grid(row=1,column=3,columnspan=3)


def current_time():
    cur_time.config(text=datetime.datetime.now().strftime("%H:%M:%S"))
    cur_time.after(1000,current_time)

cur_time=Label(root,font="18")
cur_time.grid(row=3,columnspan=3)
current_time()


hour=StringVar(root)
hours=tuple(["{:0>2}".format(i) for i in range(25)])
hour.set(hours[0])

hrs=OptionMenu(root,hour,*hours)
hrs.grid(row=3,column=3)

minute=StringVar(root)
minutes=tuple(["{:0>2}".format(i) for i in range(61)])
minute.set(minutes[0])

mins=OptionMenu(root,minute,*minutes)
mins.grid(row=3,column=4)

second=StringVar(root)
seconds=tuple(["{:0>2}".format(i) for i in range(61)])
second.set(seconds[0])

secs=OptionMenu(root,second,*seconds)
secs.grid(row=3,column=5)

Button(root,text="Set Alarm",font="Helvetica 15",command=Threading).grid(row=4,column=2,columnspan=2,pady=10)

Button(root,text="Close",font="Helvetica 12",command=root.destroy).grid(row=5,column=2,columnspan=2,pady=10)
root.mainloop()
