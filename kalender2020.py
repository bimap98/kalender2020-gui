from tkinter import *
import calendar
root = Tk()
root.title("KALENDER")
year = 2020
kalender = calendar.calendar(year)
cal_year = Label(root, text=kalender, font=("Courier",10))
cal_year.pack()
root.mainloop()
