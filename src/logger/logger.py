import time
from proglog import ProgressBarLogger
import tkinter as tk


class TkProgressBarLogger(ProgressBarLogger):
    def __init__(self, progress_bar, status_text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.progress_bar = progress_bar
        self.status_text = status_text
        self.start_time = None

    def callback(self, **changes):
        if self.start_time is None:
            self.start_time = time.time()

        if changes.get('bars') and 't' in changes['bars']:
            current_time = changes['bars']['t']['index']
            total_time = changes['bars']['t']['total']
            progress = (current_time / total_time) * 100
            self.progress_bar["value"] = progress
            self.progress_bar.update_idletasks()

            # Calcular el ETA
            elapsed_time = time.time() - self.start_time
            remaining_time = (elapsed_time / progress) * (100 - progress) if progress > 0 else 0
            eta_minutes, eta_seconds = divmod(remaining_time, 60)

            eta_message = f"ETA: {int(eta_minutes):02d}:{int(eta_seconds):02d} minutos"
            self.status_text.insert(tk.END, f"Progreso: {progress:.2f}% - {eta_message}\n")
            self.status_text.see(tk.END)
            self.status_text.update_idletasks()

        if 'message' in changes:
            self.status_text.insert(tk.END, changes['message'] + "\n")
            self.status_text.see(tk.END)
            self.status_text.update_idletasks()
