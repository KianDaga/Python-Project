from tkinter import Tk, StringVar, Entry, Button, messagebox
import time

def countdowntimer():
    try:
        user_input = int(hour.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    except:
        messagebox.showwarning("Error", "Please enter a valid hour and minute")

    while user_input > -1:
        mins, secs = divmod(user_input, 60)
        hours = 0
        if mins >= 60:
            hours, mins = divmod(mins,60)

        hour.set("{:02d}".format(hours))
        minutes.set("{:02d}".format(mins))
        seconds.set("{:02d}".format(secs))

        root.update()
        time.sleep(1)

        if user_input == 0:
            messagebox.showinfo("Time Countdown", "Time Over")

        user_input -= 1


root = Tk()
root.geometry("400x300")
root.title("Countdown Timer")
root.config(background="#345")

hour = StringVar()
minutes = StringVar()
seconds = StringVar()

hour.set("00")
minutes.set("00")
seconds.set("00")

hour_box = Entry(root, width=3, font=("Arial", 18), textvariable=hour)
minutes_box = Entry(root, width=3, font=("Arial", 18), textvariable = minutes)
seconds_box = Entry(root, width=3, font=("Arial", 18), textvariable=seconds)

hour_box.place(x=80, y=20)
minutes_box.place(x=130, y=20)
seconds_box.place(x=180, y=20)\

btn = Button(root, text= "Start Countdown", command=countdowntimer)
btn.place(x=80, y=120)
root.mainloop()

