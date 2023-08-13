from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Упс", message="Одно из полей осталось пустым")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Считываем старые данные
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Обновляем данные
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Сохраняем новые данные
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- ПОИСК ПАРОЛЕЙ ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Ошибка", message="Не найден файл")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nПароль: {password}")
        else:
            messagebox.showinfo(title="Ошибка", message=f"Нет данных с этого сервиса: {website}")


# ---------------------------- ИНТЕРФЕЙС ------------------------------- #

window = Tk()
window.title("Менеджер паролей")
window.config(padx=30, pady=30)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Надписи
website_label = Label(text="Сервис:")
website_label.grid(row=1, column=0)
email_label = Label(text="Логин:")
email_label.grid(row=2, column=0)
password_label = Label(text="Пароль:")
password_label.grid(row=3, column=0)

#Поля ввода
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=30)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "user@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

# Кнопки
search_button = Button(text="Поиск",width=15, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Сгенерировать",width=15, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Добавить", width=25, command=save)
add_button.grid(row=4, column=1)

window.mainloop()