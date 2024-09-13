import tkinter as tk
from tkinter import ttk

class ProgressBar:
    def __init__(self, root):
        """Initialize the progress bar and status text."""
        self.root = root

        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        # Status text box
        self.status_text = tk.Text(self.root, height=10, width=50)
        self.status_text.pack(pady=10)
