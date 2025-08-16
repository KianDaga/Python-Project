import tkinter as tk
from generate_password import gui_generate_password

def on_button_click():
    website = website_entry.get()
    login_id = id_entry.get()
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_special_char = special_char_var.get()
    include_numbers = numbers_var.get()
    password_length = password_length_entry.get()

    gui_generate_password(website, login_id, include_uppercase, include_lowercase, include_special_char, include_numbers, password_length)

window = tk.Tk()
window.title("Kian's Password Generator ")

website_label = tk.Label(window, text="Website:")
website_label.pack()

website_entry = tk.Entry(window)
website_entry.pack()

id_label = tk.Label(window, text="ID:")
id_label.pack()

id_entry = tk.Entry(window)
id_entry.pack()

numbers_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Numbers", variable=numbers_var).pack(padx=20)

current_value = numbers_var.get()
numbers_var.set(True)

uppercase_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(window, text="Include Uppercase", variable=uppercase_var)
checkbutton.pack()

lowercase_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(window, text="Include Lowercase", variable=lowercase_var)
checkbutton.pack(padx=20)

special_char_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(window, text="Include Special Characters", variable=special_char_var)
checkbutton.pack(padx=20)

tk.Label(window, text="Password Length:").pack(padx=20)
password_length_entry = tk.Entry(window)
password_length_entry.pack()

button = tk.Button(window, text="Generate Password", fg="black", command = on_button_click)
button.pack()

window.mainloop()