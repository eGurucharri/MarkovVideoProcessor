import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.ui.file_select import FileSelectFrame
from src.ui.filter_options import FilterOptionsFrame
from src.ui.video_settings import VideoSettingsFrame
from src.ui.progress_display import ProgressDisplayFrame
from src.ui.speed_options import SpeedOptionsFrame
from src.video_processor.video_processor import process_video
from src.config import DEFAULT_VIDEO_DIRECTORY, DEFAULT_VIDEO_DURATION, DEFAULT_SEGMENT_DURATION_MIN, DEFAULT_SEGMENT_DURATION_MAX

class VideoMarkovApp:
    def __init__(self, window):
        self.root = window
        self.root.title("Markov Video Processor")

        # Recursive variable
        self.recursive_var = tk.BooleanVar()

        ## Instantiate all frames
        self.file_select_frame = FileSelectFrame(self.root, DEFAULT_VIDEO_DIRECTORY, self.recursive_var)
        self.filters_frame = FilterOptionsFrame(self.root)
        self.video_settings_frame = VideoSettingsFrame(self.root, DEFAULT_VIDEO_DURATION, DEFAULT_SEGMENT_DURATION_MIN, DEFAULT_SEGMENT_DURATION_MAX)
        self.speed_options_frame = SpeedOptionsFrame(self.root)  # Add Speed Options Frame
        self.progress_frame = ProgressDisplayFrame(self.root)

        # Generate Video Button
        self.button_generate = ttk.Button(self.root, text="Generate Video", command=self.generate_video)
        self.button_generate.grid(pady=10, row=4, column=0, sticky="ew", padx=10)

    def generate_video(self):
        video_dir = self.file_select_frame.entry_dir.get()
        duration = int(self.video_settings_frame.entry_duration.get())
        base_name = "output_video"  # Puedes usar un widget para obtener esto también

        min_segment_duration = float(self.video_settings_frame.entry_min_segment_duration.get())
        max_segment_duration = float(self.video_settings_frame.entry_max_segment_duration.get())

        # Obtener los filtros seleccionados desde el frame simplificado de opciones de filtros
        selected_filters = self.filters_frame.get_selected_filters()

        if not selected_filters:
            result = tk.messagebox.askyesno("No Filters Selected", "Do you want to continue without applying filters?")
            if not result:
                return

        # Verificar si la opción de aplicar filtros a cada segmento está habilitada
        apply_filters_to_segments = self.filters_frame.are_filters_to_segments_enabled()

        # Verificar si la opción de aplicar solo un filtro por segmento está habilitada
        apply_one_filter_per_segment = self.filters_frame.is_one_filter_per_segment_enabled()

        # Retrieve speed options
        keep_original_speed = self.speed_options_frame.keep_original_speed.get()
        slow_down = self.speed_options_frame.slow_down.get()
        speed_up = self.speed_options_frame.speed_up.get()
        reverse_speed = self.speed_options_frame.reverse_speed.get()

        # Pass these options to the process_video function
        process_video(video_dir, duration, [".mp4"], self.progress_frame.progress, self.progress_frame.status_text,
                      selected_filters, base_name, min_segment_duration=min_segment_duration,
                      max_segment_duration=max_segment_duration, keep_original_speed=keep_original_speed,
                      slow_down=slow_down, speed_up=speed_up, reverse_speed=reverse_speed,
                      apply_filters_to_segments=apply_filters_to_segments,
                      apply_one_filter_per_segment=apply_one_filter_per_segment)


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoMarkovApp(root)
    root.mainloop()
