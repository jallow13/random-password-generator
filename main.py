from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_random():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter+password_symbols+password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    p_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = w_entry.get()
    email = e_entry.get()
    password = p_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPs",message="no field can be left empty")

    else:
        is_okay = messagebox.askokcancel(title=website,message=f"These are the details provided:\n Email: {email}\nPassword:"
                                                               f" {password}\nIs it okay to save")
        if is_okay:
            with open("data.txt",'a') as file:
                file.write(f"{website} | {email} | {password}\n")
                w_entry.delete(0,END)
                p_entry.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("passwrd manager")
screen.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
image_pic = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = image_pic)
canvas.grid(row=0,column=1)

web = Label(text="Website:")
web.grid(row=1,column=0)
email = Label(text="Email/Username:")
email.grid(row=2,column=0)
password = Label(text="Password:")
password.grid(row=3,column=0)

w_entry = Entry(width=53)
w_entry.focus()
w_entry.grid(row=1,column=1,columnspan=2)
e_entry = Entry(width=53)
e_entry.insert(0,"howareyou@gmail.com")
e_entry.grid(row=2,column=1,columnspan=2)
p_entry = Entry(width=33)
p_entry.grid(row=3,column=1)


g_button = Button(text="Generate Password",command=generate_random)
g_button.grid(row=3,column=2)

g_button = Button(text="Add",width=39,command=save_data)
g_button.grid(row=4,column=1,columnspan=2)


screen.mainloop()