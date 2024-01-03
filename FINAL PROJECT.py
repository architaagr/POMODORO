# default timer
# ui ux
# pause button

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
from tkinter import *

 
# Create the main application window
window = tk.Tk()
window.config(bg = '#9fc5e8')
root = Frame(window,bg="#9fc5e8")

# Create a StringVar to hold the selected option
selected_option = tk.StringVar()

# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()
  
# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

def work():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = 6
    except:
        print("Please input the right value")
    global the_value
    the_value = lb.get(lb.curselection())
    try:
        current_task_msg=tk.Label(window,text="You are working on: \n"+the_value, font=("times",15), bg="teal")
        current_task_msg.place(x=420,y=190)
        #current_session_msg=tk.Label(window,text="current session: "+rounds)
        #current_session_msg.place(x=20,y=30)
    except:
        messagebox.showinfo("Select task", "Please select a task to continue")
    for rounds in range (1,5):
        r=str(rounds)
        rounds=tk.Label(window,text="You are on round "+r, font=("times",15), bg="teal")
        rounds.place(x=600,y=190)
        temp=6
        while temp >-1:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60) 
            # Converting the input entered in mins or secs to hours, mins ,secs
            # (input = 110 min --> 110*60 = 6600sec => 1hr : 50min: 0sec)
            hours=0
            if mins >60:
                
                # divmod(firstvalue = temp//60, secondvalue 
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            # using format () method to store the value up to 
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
            

            # updating the GUI window after decrementing the
            # temp value every time
            window.update()
            time.sleep(1)
            
            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                messagebox.showinfo("Work time", "Good Job! Time to take a break")
            temp -= 1
        rounds.destroy()
    else:
        messagebox.showinfo("Time", "Good Job! Time to take a long break, see ya!")
        rounds.destroy()
        current_task_msg.destroy()

def takebreak():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = 5
        current_task_msg=tk.Label(window,text="You are on a break: \n Do something fun!", font=("times",15,), bg="teal")
        current_task_msg.place(x=545,y=190)
    except:
        print("Please input the right value")
    
    while temp >-1:
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60) 
        # Converting the input entered in mins or secs to hours, mins ,secs
        # (input = 110 min --> 110*60 = 6600sec => 1hr : 50min: 0sec)
        hours=0
        if mins >60:
            
            # divmod(firstvalue = temp//60, secondvalue 
            # = temp%60)
            hours, mins = divmod(mins, 60)
        
        # using format () method to store the value up to 
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        

        # updating the GUI window after decrementing the
        # temp value every time
        window.update()
        time.sleep(1)
        
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Break Time", "Time to get back to work")
            current_task_msg.destroy()
        
        # after every one sec the value of temp will be decremented by one
        temp -= 1


hourEntry= Entry(root, width=3, font=("times",70,""), textvariable=hour)
hourEntry.place(x=130, y=70)
  
minuteEntry= Entry(root, width=3, font=("times",70,""), textvariable=minute)
minuteEntry.place(x=310, y=70)

secondEntry= Entry(root, width=3, font=("times",70,""), textvariable=second)
secondEntry.place(x=490, y=70)

# button widget break
breakbtn = Button(root, text='Start break', bd='5', font =("times",13), command= takebreak)
breakbtn.pack(side='bottom', pady=5)
root.pack(ipadx=250, ipady=100,fill=Y)

# button widget work
startbtn = Button(root, text='Start work', bd='5', font =("times",13), command= work)
startbtn.pack(side='bottom', pady=5)
root.pack(ipadx=250, ipady=100,fill=Y)

# Create the main window
window.title("POMODORO TIMER")

# Left Frame (Progress Tracker and Task Organizer)
'''left_frame = tk.Frame(window)

task_list = tk.Listbox(left_frame, selectmode=tk.SINGLE)
task_list.pack(fill=tk.BOTH)'''

# Middle Frame (Timer and Start/Stop Button)
middle_frame = tk.Frame(window)
middle_frame.pack()

timer_label = tk.Label(root, text='POMODORO TIMER', font=("times", 25))
timer_label.pack(side='top')

# Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size to match the screen
window.geometry(f"{screen_width}x{screen_height}")

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
ws = Frame(window)
ws.configure(bg="#FAEBD7")

frame = Frame(ws)
frame.pack()

lb = Listbox(
    frame,
    width=52,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = ['task 1','task 2']

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack()

button_frame = Frame(ws)
button_frame.pack()

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=False, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=False, side=LEFT)
task_title = Label(window,text='TASK MANAGER',font=('times 20'))
task_title.place(x=550,y=335)

ws.place(x=360,y=340,height=300,width=645)

#task_title.place(x=550,y=335)
#ws.place(x=360,y=345)

# Main loop
window.mainloop()
