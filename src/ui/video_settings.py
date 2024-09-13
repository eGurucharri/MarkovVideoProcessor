import tkinter as tk
from tkinter import ttk


class VideoSettingsFrame(ttk.LabelFrame):
    def __init__(self, parent, default_duration, min_segment_duration, max_segment_duration):
        super().__init__(parent, text="Video Settings", padding=(10, 5))
        # Cambia fill="x" por sticky="ew" para expandirse horizontalmente
        self.grid(padx=10, pady=5, sticky="ew")

        # Duración del archivo final
        self.label_duration = ttk.Label(self, text="Video Duration (seconds):")
        self.label_duration.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.entry_duration = ttk.Entry(self, width=10)
        self.entry_duration.insert(0, str(default_duration))
        self.entry_duration.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        # Duración mínima de los cortes
        self.label_min_segment_duration = ttk.Label(self, text="Minimum Segment Duration (seconds):")
        self.label_min_segment_duration.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.entry_min_segment_duration = ttk.Entry(self, width=10)
        self.entry_min_segment_duration.insert(0, str(min_segment_duration))
        self.entry_min_segment_duration.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        # Duración máxima de los cortes
        self.label_max_segment_duration = ttk.Label(self, text="Maximum Segment Duration (seconds):")
        self.label_max_segment_duration.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.entry_max_segment_duration = ttk.Entry(self, width=10)
        self.entry_max_segment_duration.insert(0, str(max_segment_duration))
        self.entry_max_segment_duration.grid(row=2, column=1, sticky="w", padx=5, pady=5)
