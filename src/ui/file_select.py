import tkinter as tk
from tkinter import ttk, filedialog

class FileSelectFrame(ttk.LabelFrame):
    def __init__(self, parent, default_directory, recursive_var):
        super().__init__(parent, text="Select Folder", padding=(10, 5))
        self.grid(padx=10, pady=5, sticky="ew")  # Cambiamos 'fill="x"' por 'sticky="ew"'

        self.label_dir = ttk.Label(self, text="Video folder:")
        self.label_dir.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entry_dir = ttk.Entry(self, width=50)
        self.entry_dir.insert(0, default_directory)
        self.entry_dir.grid(row=0, column=1, padx=5, pady=5)

        self.button_browse = ttk.Button(self, text="Browse", command=self.browse_folder)
        self.button_browse.grid(row=0, column=2, padx=5, pady=5)

        self.check_recursive = ttk.Checkbutton(self, text="Search recursively", variable=recursive_var)
        self.check_recursive.grid(row=1, column=1, sticky="w")

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.entry_dir.delete(0, tk.END)
            self.entry_dir.insert(0, folder_selected)
