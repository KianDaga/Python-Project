import string 
import random 
from tkinter import messagebox

def gui_generate_password(website, login_id, include_uppercase, include_lowercase, include_special_char, include_numbers, password_length):
    password = ""
    if include_uppercase:
        password += string.ascii_uppercase
    if include_lowercase:
        password += string.ascii_lowercase
    if include_special_char:
        password += string.punctuation
    if include_numbers:
        password += string.digits
    if not password:
        messagebox.showinfo("Error ", "Please select at least one character type.")
        return 
    try:
        password_length = int(password_length)
    except ValueError:
        messagebox.showinfo("Error", "Please enter a valid password length.")
        return
    
    password = ''.join(random.choice(password) for i in range(password_length))  
    with open("passwords.txt", "a") as file:
        file.write(f"Website: {website}\nLogin ID: {login_id}\nPassword: {password}\n\n")

        messagebox.showinfo("Password Generated", f"Password: {password}")

   
