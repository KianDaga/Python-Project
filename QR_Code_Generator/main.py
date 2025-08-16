import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image

def generate_qr():
    website = url_entry.get().strip()
    filename = filename_entry.get().strip()
    print(f"Website: {website}, Filename: {filename}")

    if website and filename:
        filepath = filename + ".png"
        qr = qrcode.make(website)
        qr.save(filepath)

        show_qr_code(filepath, website)

        messagebox.showinfo("Success", f"QR code saved as {filepath}")
    else:
        messagebox.error("Warning", "Please enter both website URL and filename.")

def show_qr_code(img_path, website):   
    try:
        img = Image.open(img_path)
        img.show()
        print(f"This QR code points to {website}")
    except Exception as e:
        print(f"An error occurred: {e}") 

                


window = tk.Tk()
window.title("QR Code Generator")

tk.Label(window, text="Website").pack()
url_entry = tk.Entry(window)
url_entry.pack(padx=20, pady=5)

tk.Label(window, text="File name of QR Code").pack()
filename_entry = tk.Entry(window)
filename_entry.pack(padx=20, pady=5)

generate_button = tk.Button(window, text="Generate QR Code", command = generate_qr)
generate_button.pack(pady=10)

window.mainloop()

