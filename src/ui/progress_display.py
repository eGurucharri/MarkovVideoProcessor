import tkinter as tk
from tkinter import ttk

class ProgressDisplayFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Progress", padding=(10, 5))
        # Cambia fill="x" por sticky="ew"
        self.grid(padx=10, pady=5, sticky="ew")

        # Barra de progreso
        self.progress = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Texto de estado
        self.status_text = tk.Text(self, height=10, width=50)
        self.status_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
