import customtkinter as ctk
from tkinter import messagebox
import sqlite3
import subprocess

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Login")
app.geometry("450x500")
app.resizable(False, False)


def login():

    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM admin WHERE username=? AND password=?",
        (username, password)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Success", "Login Successful")
        app.destroy()

        subprocess.run(["python", "app.py"])

    else:
        messagebox.showerror("Error", "Invalid Username or Password")


title = ctk.CTkLabel(
    app,
    text="FACE RECOGNITION\nATTENDANCE SYSTEM",
    font=("Arial", 24, "bold")
)
title.pack(pady=30)

username_entry = ctk.CTkEntry(
    app,
    width=280,
    placeholder_text="Username"
)
username_entry.pack(pady=15)

password_entry = ctk.CTkEntry(
    app,
    width=280,
    placeholder_text="Password",
    show="*"
)
password_entry.pack(pady=15)

login_btn = ctk.CTkButton(
    app,
    text="LOGIN",
    width=280,
    height=40,
    command=login
)
login_btn.pack(pady=30)

app.mainloop()