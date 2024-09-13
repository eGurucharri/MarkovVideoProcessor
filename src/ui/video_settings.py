import tkinter as tk
from tkinter import filedialog
from src.config.config import DEFAULT_VIDEO_DIRECTORY, DEFAULT_VIDEO_DURATION, DEFAULT_SEGMENT_DURATION_MIN, DEFAULT_SEGMENT_DURATION_MAX

class VideoSettings:
    def __init__(self, root):
        """Initialize the video settings section."""
        self.root = root

        # Video Directory
        self.label_dir = tk.Label(root, text="Video Directory:")
        self.label_dir.pack()
        self.entry_dir = tk.Entry(root, width=50)
        self.entry_dir.insert(0, DEFAULT_VIDEO_DIRECTORY)
        self.entry_dir.pack()
        self.button_browse = tk.Button(root, text="Browse", command=self.browse_folder)
        self.button_browse.pack()

        # Duration
        self.label_duration = tk.Label(root, text="Final Video Duration (seconds):")
        self.label_duration.pack()
        self.entry_duration = tk.Entry(root, width=10)
        self.entry_duration.insert(0, str(DEFAULT_VIDEO_DURATION))
        self.entry_duration.pack()

        # Segment Duration
        self.label_min_segment_duration = tk.Label(root, text="Min Segment Duration (seconds):")
        self.label_min_segment_duration.pack()
        self.entry_min_segment_duration = tk.Entry(root, width=10)
        self.entry_min_segment_duration.insert(0, str(DEFAULT_SEGMENT_DURATION_MIN))
        self.entry_min_segment_duration.pack()

        self.label_max_segment_duration = tk.Label(root, text="Max Segment Duration (seconds):")
        self.label_max_segment_duration.pack()
        self.entry_max_segment_duration = tk.Entry(root, width=10)
        self.entry_max_segment_duration.insert(0, str(DEFAULT_SEGMENT_DURATION_MAX))
        self.entry_max_segment_duration.pack()

        # Output File Name
        self.label_output = tk.Label(root, text="Output File Name:")
        self.label_output.pack()
        self.entry_output = tk.Entry(root, width=50)
        self.entry_output.insert(0, "output")
        self.entry_output.pack()

    def get_video_settings(self):
        """Retrieve the video settings from the inputs."""
        return (
            self.entry_dir.get(),
            int(self.entry_duration.get()),
            self.entry_output.get(),
            float(self.entry_min_segment_duration.get()),
            float(self.entry_max_segment_duration.get())
        )

    def browse_folder(self):
        """Open a folder selection dialog."""
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.entry_dir.delete(0, tk.END)
            self.entry_dir.insert(0, folder_selected)
