from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- ГЕНЕРАТОР ПАРОЛЯ ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- СОХРАНЕНИЕ ПАРОЛЯ ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Упс", message="Пожайлуста заполните пустое поле")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Ваши данные: \nЛогин: {email} "
                                                      f"\nПароль: {password} \nСохранить?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- ИНТЕРФЕЙС ------------------------------- #

window = Tk()
window.title("Менеджер паролей")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Сервис:")
website_label.grid(row=1, column=0)
email_label = Label(text="Имя пользователя:")
email_label.grid(row=2, column=0)
password_label = Label(text="Пароль:")
password_label.grid(row=3, column=0)


website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)


generate_password_button = Button(text="Сгенерировать",width=35, command=generate_password)
generate_password_button.grid(row=4, column=1, columnspan=2)
add_button = Button(text="Добавить", width=35, command=save)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()