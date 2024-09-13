import tkinter as tk
from src.ui.video_settings import VideoSettings
from src.ui.filter_options import FilterOptions
from src.ui.progress_bar import ProgressBar
from src.utils.utils import show_message
from src.video_processor.video_processor import process_video

class VideoMarkovApp:
    def __init__(self, root):
        """Initialize the main window with different sections."""
        self.root = root
        self.root.title("Accessible Markov Video Generator")

        # Setup different sections of the UI
        self.video_settings = VideoSettings(root)
        self.filter_options = FilterOptions(root)
        self.progress_bar = ProgressBar(root)

        # Generate button
        self.button_generate = tk.Button(root, text="Generate Video", command=self.generate_video)
        self.button_generate.pack()

    def generate_video(self):
        """Handle video generation."""
        video_dir, duration, base_name, min_segment, max_segment = self.video_settings.get_video_settings()
        selected_filters = self.filter_options.get_selected_filters()
        apply_random_filters, apply_on_cuts, combine_filters = self.filter_options.get_filter_options()

        if not selected_filters:
            if not show_message("No Filters Selected", "No filters selected. Continue without applying filters?"):
                return

        process_video(
            video_dir=video_dir,
            total_duration=duration,
            formats=[".mp4"],
            progress_bar=self.progress_bar.progress,
            status_text=self.progress_bar.status_text,
            selected_filters=selected_filters,
            base_name=base_name,
            apply_random_filters=apply_random_filters,
            apply_on_cuts=apply_on_cuts,
            combine_filters=combine_filters,
            min_segment_duration=min_segment,
            max_segment_duration=max_segment
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoMarkovApp(root)
    root.mainloop()
