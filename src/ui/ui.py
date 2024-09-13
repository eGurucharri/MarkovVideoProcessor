import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from src.video_processor.video_processor import process_video
from src.config import DEFAULT_VIDEO_DIRECTORY, DEFAULT_VIDEO_DURATION, DEFAULT_SEGMENT_DURATION_MIN, DEFAULT_SEGMENT_DURATION_MAX

class VideoMarkovApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Video Markoviano Accesible")

        # Carpeta de videos
        self.label_dir = tk.Label(root, text="Carpeta de vídeos:")
        self.label_dir.pack()

        self.entry_dir = tk.Entry(root, width=50)
        self.entry_dir.insert(0, DEFAULT_VIDEO_DIRECTORY)
        self.entry_dir.pack()

        self.button_browse = tk.Button(root, text="Explorar", command=self.browse_folder)
        self.button_browse.pack()

        # Duración del video
        self.label_duration = tk.Label(root, text="Duración del archivo final (segundos):")
        self.label_duration.pack()

        self.entry_duration = tk.Entry(root, width=10)
        self.entry_duration.insert(0, str(DEFAULT_VIDEO_DURATION))
        self.entry_duration.pack()

        # Duración mínima del corte
        self.label_min_segment_duration = tk.Label(root, text="Duración mínima de los cortes (segundos):")
        self.label_min_segment_duration.pack()

        self.entry_min_segment_duration = tk.Entry(root, width=10)
        self.entry_min_segment_duration.insert(0, str(DEFAULT_SEGMENT_DURATION_MIN))
        self.entry_min_segment_duration.pack()

        # Duración máxima del corte
        self.label_max_segment_duration = tk.Label(root, text="Duración máxima de los cortes (segundos):")
        self.label_max_segment_duration.pack()

        self.entry_max_segment_duration = tk.Entry(root, width=10)
        self.entry_max_segment_duration.insert(0, str(DEFAULT_SEGMENT_DURATION_MAX))
        self.entry_max_segment_duration.pack()

        # Nombre del archivo de salida
        self.label_output = tk.Label(root, text="Nombre del archivo de salida:")
        self.label_output.pack()

        self.entry_output = tk.Entry(root, width=50)
        self.entry_output.insert(0, "output")
        self.entry_output.pack()

        # Sección de filtros (similar a la actual)
        self.setup_filter_options()

        # Barra de progreso
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)


        # Cuadro de texto para mostrar el estado
        self.status_text = tk.Text(root, height=10, width=50)
        self.status_text.pack(pady=10)

        # Botón para generar el video
        self.button_generate = tk.Button(root, text="Generar Video", command=self.generate_video)
        self.button_generate.pack()

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.entry_dir.delete(0, tk.END)
            self.entry_dir.insert(0, folder_selected)

    def setup_filter_options(self):
        # Filtros de color
        self.label_filter = tk.Label(self.root, text="Seleccionar filtros de color:")
        self.label_filter.pack()

        # Casillas de verificación para cada filtro
        self.filter_red = tk.BooleanVar()
        self.filter_green = tk.BooleanVar()
        self.filter_blue = tk.BooleanVar()
        self.filter_sepia = tk.BooleanVar()
        self.filter_blackwhite = tk.BooleanVar()
        self.filter_invert = tk.BooleanVar()
        self.filter_glitch = tk.BooleanVar()

        self.check_red = tk.Checkbutton(self.root, text="Rojo", variable=self.filter_red)
        self.check_green = tk.Checkbutton(self.root, text="Verde", variable=self.filter_green)
        self.check_blue = tk.Checkbutton(self.root, text="Azul", variable=self.filter_blue)
        self.check_sepia = tk.Checkbutton(self.root, text="Sepia", variable=self.filter_sepia)
        self.check_blackwhite = tk.Checkbutton(self.root, text="Blanco y Negro", variable=self.filter_blackwhite)
        self.check_invert = tk.Checkbutton(self.root, text="Invertir colores", variable=self.filter_invert)
        self.check_glitch = tk.Checkbutton(self.root, text="Glitch", variable=self.filter_glitch)

        self.check_red.pack(anchor=tk.W)
        self.check_green.pack(anchor=tk.W)
        self.check_blue.pack(anchor=tk.W)
        self.check_sepia.pack(anchor=tk.W)
        self.check_blackwhite.pack(anchor=tk.W)
        self.check_invert.pack(anchor=tk.W)
        self.check_glitch.pack(anchor=tk.W)

        # Opción para aplicar filtros aleatorios
        self.random_filters = tk.BooleanVar()
        self.check_random_filters = tk.Checkbutton(self.root, text="Aplicar filtros a intervalos aleatorios", variable=self.random_filters)
        self.check_random_filters.pack()

        # Opción para aplicar filtros en los cortes realizados
        self.apply_on_cuts = tk.BooleanVar()
        self.check_apply_on_cuts = tk.Checkbutton(self.root, text="Aplicar filtros en los cortes realizados", variable=self.apply_on_cuts)
        self.check_apply_on_cuts.pack()

        # Opción para combinar filtros
        self.combine_filters = tk.BooleanVar()
        self.check_combine_filters = tk.Checkbutton(self.root, text="Combinar filtros seleccionados", variable=self.combine_filters)
        self.check_combine_filters.pack()

    def generate_video(self):
        video_dir = self.entry_dir.get()
        duration = int(self.entry_duration.get())
        base_name = self.entry_output.get()

        # Obtener duraciones de cortes
        min_segment_duration = float(self.entry_min_segment_duration.get())
        max_segment_duration = float(self.entry_max_segment_duration.get())

        apply_random_filters = self.random_filters.get()
        apply_on_cuts = self.apply_on_cuts.get()
        combine_filters = self.combine_filters.get()

        # Listado de filtros seleccionados
        selected_filters = []
        if self.filter_red.get():
            selected_filters.append('red')
        if self.filter_green.get():
            selected_filters.append('green')
        if self.filter_blue.get():
            selected_filters.append('blue')
        if self.filter_sepia.get():
            selected_filters.append('sepia')
        if self.filter_blackwhite.get():
            selected_filters.append('black_and_white')
        if self.filter_invert.get():
            selected_filters.append('invert')
        if self.filter_glitch.get():
            selected_filters.append('glitch')

        # Permitir procesar el video sin filtros
        if not selected_filters:
            result = messagebox.askyesno("Sin filtros",
                                         "No se ha seleccionado ningún filtro. ¿Desea continuar sin aplicar filtros?")
            if not result:
                return

        process_video(video_dir, duration, [".mp4"], self.progress, self.status_text, selected_filters, base_name,
                      apply_random_filters=apply_random_filters, apply_on_cuts=apply_on_cuts, combine_filters=combine_filters,
                      min_segment_duration=min_segment_duration, max_segment_duration=max_segment_duration)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoMarkovApp(root)
    root.mainloop()
