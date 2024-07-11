from tkinter import *
import random


def pass_generator():
    pass_text.delete(0, END)
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(num_letters)]
    password_num = [random.choice(numbers) for _ in range(num_numbers)]
    password_symbol = [random.choice(symbols) for _ in range(num_symbols)]

    password_list = password_letters + password_num + password_symbol
    random.shuffle(password_list)
    s_password = "".join(password_list)
    pass_text.insert(END, s_password)


window = Tk()
window.title("Password Generator")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
password = Label(text="Password")
password.grid(column=0, row=1)
pass_text = Entry(width=30)
pass_text.grid(column=1,row=1)
pass_generator = Button(text="Generate Password", width=15,command=pass_generator)
pass_generator.grid(column=1, row=3)

window.mainloop()