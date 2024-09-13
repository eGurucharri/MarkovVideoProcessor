import tkinter as tk
from src.ui.ui import VideoMarkovApp

def test_ui_initialization():
    root = tk.Tk()
    app = VideoMarkovApp(root)
    assert app is not None
