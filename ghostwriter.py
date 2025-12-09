"""Ghostwriter"""
from tkinter import Tk, Label, Entry, Button, DISABLED, ACTIVE

import pyautogui


BTN_START_TEXT = 'Introduce text to ghost write'

def run():
    def ghost_write():
        update_in = 'Writing in %s seconds...'
        btn.config(state=DISABLED)
        try:
            seconds = int(e2.get())
        except ValueError:
            seconds = 5

        def tick(i):
            if i > 0:
                btn.config(text=update_in % i)
                root.after(1000, tick, i-1)
            else:
                btn.config(text='Writing...')

                pyautogui.write(e1.get())
                btn.config(text='Done!')
                reactivate()

        tick(seconds)

    def reactivate():

        def tick(i=1):
            if i>0:
                root.after(1000, tick, i-1)
            else:
                btn.config(state=ACTIVE, text=BTN_START_TEXT)
        tick()





    root = Tk()
    root.title('Ghostwriter')

    Label(root, text=BTN_START_TEXT).grid(row=0)
    e1 = Entry(root)
    e1.grid(row=0, column=1)

    Label(root, text="Delay (s)").grid(row=1)
    e2 = Entry(root)
    e2.grid(row=1, column=1)
    e2.insert(0, "5")

    btn = Button(root, text='Ghostwrite', width=25, command=ghost_write)
    btn.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()
