import tkinter as tk
from tkinter import messagebox
import threading
import time
import pydirectinput  # Changed from pyautogui
import keyboard

class AutoPresser:
    def __init__(self, master):
        self.master = master
        master.title("Automated Key Presser")

        self.running = False

        tk.Label(master, text="Key to Press:").grid(row=0, column=0, padx=5, pady=5)
        self.key_entry = tk.Entry(master, width=10)
        self.key_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(master, text="Press Duration (seconds):").grid(row=1, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(master, width=10)
        self.duration_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(master, text="Interval (seconds):").grid(row=2, column=0, padx=5, pady=5)
        self.interval_entry = tk.Entry(master, width=10)
        self.interval_entry.grid(row=2, column=1, padx=5, pady=5)

        self.start_button = tk.Button(master, text="Start (F8)", command=self.start_pressing, width=15, bg='lightgreen')
        self.start_button.grid(row=3, column=0, padx=5, pady=5)

        self.stop_button = tk.Button(master, text="Stop (F9)", command=self.stop_pressing, width=15, bg='salmon')
        self.stop_button.grid(row=3, column=1, padx=5, pady=5)

        keyboard.add_hotkey('F8', self.start_pressing)
        keyboard.add_hotkey('F9', self.stop_pressing)

    def press_loop(self, key, duration, interval):
        while self.running:
            pydirectinput.keyDown(key)  # Changed here
            time.sleep(duration)
            pydirectinput.keyUp(key)    # Changed here
            time.sleep(interval)

    def start_pressing(self):
        if self.running:
            messagebox.showinfo("Info", "Already running!")
            return

        key = self.key_entry.get()
        try:
            duration = float(self.duration_entry.get())
            interval = float(self.interval_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Duration and interval must be numbers!")
            return

        self.running = True
        threading.Thread(target=self.press_loop, args=(key, duration, interval), daemon=True).start()

    def stop_pressing(self):
        if self.running:
            self.running = False
            messagebox.showinfo("Info", "Stopped!")
        else:
            messagebox.showinfo("Info", "Not running!")

root = tk.Tk()
app = AutoPresser(root)
root.mainloop()
