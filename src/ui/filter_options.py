import tkinter as tk
from tkinter import ttk

class FilterOptionsFrame(ttk.LabelFrame):
    def __init__(self, parent):
        # Inicializa el marco de opciones de filtro, con un título y un poco de padding
        super().__init__(parent, text="Filter Options", padding=(10, 5))
        # Configura el widget para ocupar all el espacio horizontal disponible
        self.grid(padx=10, pady=5, sticky="ew")

        # Variables booleanas para cada filtro (serán vinculadas a los checkboxes)
        self.filter_red = tk.BooleanVar()
        self.filter_green = tk.BooleanVar()
        self.filter_blue = tk.BooleanVar()
        self.filter_sepia = tk.BooleanVar()
        self.filter_blackwhite = tk.BooleanVar()
        self.filter_invert = tk.BooleanVar()
        self.filter_glitch = tk.BooleanVar()

        # Creación de los checkboxes para los filtros de color
        self.check_red = ttk.Checkbutton(self, text="Red", variable=self.filter_red)
        self.check_red.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.check_green = ttk.Checkbutton(self, text="Green", variable=self.filter_green)
        self.check_green.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        self.check_blue = ttk.Checkbutton(self, text="Blue", variable=self.filter_blue)
        self.check_blue.grid(row=0, column=2, sticky="w", padx=5, pady=5)

        # Filtros adicionales: sepia, blanco y negro, invertir colores, glitch
        self.check_sepia = ttk.Checkbutton(self, text="Sepia", variable=self.filter_sepia)
        self.check_sepia.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.check_blackwhite = ttk.Checkbutton(self, text="Black and White", variable=self.filter_blackwhite)
        self.check_blackwhite.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        self.check_invert = ttk.Checkbutton(self, text="Invert Colors", variable=self.filter_invert)
        self.check_invert.grid(row=1, column=2, sticky="w", padx=5, pady=5)

        self.check_glitch = ttk.Checkbutton(self, text="Glitch", variable=self.filter_glitch)
        self.check_glitch.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        # Opción para aplicar filtros de forma aleatoria en intervalos
        self.random_filters = tk.BooleanVar()
        self.check_random_filters = ttk.Checkbutton(self, text="Apply filters at random intervals", variable=self.random_filters)
        self.check_random_filters.grid(row=3, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        # Opción para aplicar filtros en los cortes entre segmentos
        self.apply_on_cuts = tk.BooleanVar()
        self.check_apply_on_cuts = ttk.Checkbutton(self, text="Apply filters on cuts", variable=self.apply_on_cuts)
        self.check_apply_on_cuts.grid(row=4, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        # Opción para combinar los filtros seleccionados
        self.combine_filters = tk.BooleanVar()
        self.check_combine_filters = ttk.Checkbutton(self, text="Combine selected filters", variable=self.combine_filters)
        self.check_combine_filters.grid(row=5, column=0, columnspan=3, sticky="w", padx=5, pady=5)
