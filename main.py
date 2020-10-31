from tkinter import *
import pyperclip
import string
import random

root = Tk()
root.geometry("400x210")
root.config(bg="#7DF9FF")
root.wm_maxsize(400,210)
root.title("Password Generator")

Label(root, text='PASSWORD GENERATOR', font= 'arial 15 bold', fg= "black").pack()

pass_label = Label(root, text= 'Password Length', font = 'arial 15 bold', fg= "black").pack()
passLen = IntVar()

length = Spinbox(root, from_ = 4, to_ = 32,
                 textvariable= passLen, width= 15).pack()

#Function to generate password
password_string = StringVar()

def Generator():
    password = ''

    for x in range(0,100):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
        for y in range(passLen.get() - 4):
                password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        password_string.set(password)

Button(root, text= "Generate Password", command = Generator).pack(pady= 5)

Entry(root, textvariable= password_string).pack()

def Copy_password():
    pyperclip.copy(password_string.get())

Button(root, text= 'Copy to Clipboard', command = Copy_password).pack(pady= 5)

quit_button = Button(root, text= 'Quit', command= quit).place(y= 85)

root.mainloop()