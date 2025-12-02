from tkinter import *

def submit():
    root.destroy()

root = Tk()
root.geometry("600x600")
root.title("Personal info")
root.config(bg="lightblue")

heading = Label(root, text="Personal Info", font=("Arial", 50), bg="lightblue")
heading.pack()

name = Label(root, text="Name:", font=("Arial", 20), bg="lightblue")
name.place(y=75, x=50)

namein = Entry(root, font=("Arial", 20), width=20)
namein.place(x=250, y=75)

gender = Label(root, text="Gender:", font=("Arial", 20), bg="lightblue")
gender.place(y=150, x=50)

genderin = Entry(root, font=("Arial", 20), width=20)
genderin.place(x=250, y=150)

enter = Button(root, text="Enter", font=("Arial", 20), command=submit)
enter.place(y=225, x=150)

root.mainloop()