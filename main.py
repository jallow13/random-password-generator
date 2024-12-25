from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

# ---------------------------- SEARCHING FOR PASSWORD  ------------------------------- #

def find_password():
    key = w_entry.get()
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")
    else:
        if key in data:
            email = data[key]["Email: "]
            password = data[key]["Password: "]
            messagebox.showinfo(title=key, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title=key,message=f"Website {key} doesnt exist")


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

    json_data ={
        website:{
        "Email: ":email,
        "Password: ":password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPs",message="no field can be left empty")

    else:
        try:
            with open("data.json",'r') as file:
                #LOADING(READING)
                data=json.load(file)

        except:
            with open("data.json","w") as file:
                #writng the new updated data
                json.dump(json_data,file,indent=4)
        else:
            # UPDATING
            data.update(json_data)

            with open("data.json","w") as file:
                #writng the new updated data
                json.dump(data,file,indent=4)
        finally:
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

w_entry = Entry(width=35)
w_entry.focus()
w_entry.grid(row=1,column=1)
e_entry = Entry(width=53)
e_entry.insert(0,"howareyou@gmail.com")
e_entry.grid(row=2,column=1,columnspan=2)
p_entry = Entry(width=33)
p_entry.grid(row=3,column=1)


g_button = Button(text="Generate Password",command=generate_random)
g_button.grid(row=3,column=2)

g_button = Button(text="Add",width=39,command=save_data)
g_button.grid(row=4,column=1,columnspan=2)

s_button = Button(text="search",width=17,command=find_password)
s_button.grid(row=1,column=2)


screen.mainloop()