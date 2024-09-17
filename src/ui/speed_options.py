import tkinter as tk
from tkinter import ttk

class SpeedOptionsFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Speed Options", padding=(10, 5))
        self.grid(padx=10, pady=5, sticky="ew")

        # Variables to store the states
        self.keep_original_speed = tk.BooleanVar()
        self.slow_down = tk.BooleanVar()
        self.speed_up = tk.BooleanVar()
        self.reverse_speed = tk.BooleanVar()

        # Checkbox for keeping original speeds
        self.check_keep_original = ttk.Checkbutton(self, text="Keep original speeds", variable=self.keep_original_speed)
        self.check_keep_original.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)

        # Options to modify speeds
        self.check_slow_down = ttk.Checkbutton(self, text="Slow down cuts", variable=self.slow_down)
        self.check_slow_down.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.check_speed_up = ttk.Checkbutton(self, text="Speed up cuts", variable=self.speed_up)
        self.check_speed_up.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        self.check_reverse_speed = ttk.Checkbutton(self, text="Reverse speeds", variable=self.reverse_speed)
        self.check_reverse_speed.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        # Disable the other options when keeping original speeds
        self.keep_original_speed.trace("w", self.toggle_speed_options)

    def toggle_speed_options(self, *args):
        if self.keep_original_speed.get():
            self.check_slow_down.config(state="disabled")
            self.check_speed_up.config(state="disabled")
            self.check_reverse_speed.config(state="disabled")
        else:
            self.check_slow_down.config(state="normal")
            self.check_speed_up.config(state="normal")
            self.check_reverse_speed.config(state="normal")
