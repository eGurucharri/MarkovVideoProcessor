import tkinter as tk
from tkinter import ttk

class FilterOptionsFrame(ttk.LabelFrame):
    def __init__(self, parent):
        """Inicializa el marco de opciones de filtro, con un título y un poco de padding."""
        super().__init__(parent, text="Filter Options", padding=(10, 5))
        self.grid(padx=10, pady=5, sticky="ew")

        # Variables booleanas para cada filtro (vinculadas a los checkboxes)
        self.filter_vars = {
            'red': tk.BooleanVar(),
            'green': tk.BooleanVar(),
            'blue': tk.BooleanVar(),
            'sepia': tk.BooleanVar(),
            'black_and_white': tk.BooleanVar(),
            'invert': tk.BooleanVar(),
            'glitch': tk.BooleanVar()
        }

        # Asignar los filtros a los checkbuttons
        filters = [
            ('Red', 'red'), ('Green', 'green'), ('Blue', 'blue'),
            ('Sepia', 'sepia'), ('Black and White', 'black_and_white'),
            ('Invert Colors', 'invert'), ('Glitch', 'glitch')
        ]
        for i, (text, key) in enumerate(filters):
            ttk.Checkbutton(self, text=text, variable=self.filter_vars[key]).grid(row=i//3, column=i%3, sticky="w", padx=5, pady=5)

        # Opción para aplicar filtros a cada segmento
        self.apply_filters_to_segments = tk.BooleanVar()
        ttk.Checkbutton(self, text="Apply filters to each segment", variable=self.apply_filters_to_segments).grid(row=3, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        # Opción para aplicar solo un filtro por segmento
        self.apply_one_filter_per_segment = tk.BooleanVar()
        ttk.Checkbutton(self, text="Apply only one filter per segment", variable=self.apply_one_filter_per_segment).grid(row=4, column=0, columnspan=3, sticky="w", padx=5, pady=5)

    def get_selected_filters(self):
        """Devuelve una lista de los filtros seleccionados por el usuario."""
        selected_filters = [filter_name for filter_name, var in self.filter_vars.items() if var.get()]
        return selected_filters

    def are_filters_to_segments_enabled(self):
        """Devuelve True si la opción de aplicar filtros a cada segmento está habilitada."""
        return self.apply_filters_to_segments.get()

    def is_one_filter_per_segment_enabled(self):
        """Devuelve True si la opción de aplicar solo un filtro por segmento está habilitada."""
        return self.apply_one_filter_per_segment.get()
