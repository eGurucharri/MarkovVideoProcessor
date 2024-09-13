import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.ui.main_window import VideoMarkovApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoMarkovApp(root)
    root.mainloop()
