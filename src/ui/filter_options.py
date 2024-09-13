import tkinter as tk

class FilterOptions:
    def __init__(self, root):
        """Initialize the filter options section."""
        self.root = root
        self.label_filter = tk.Label(self.root, text="Select Color Filters:")
        self.label_filter.pack()

        self.filter_vars = {
            'red': tk.BooleanVar(),
            'green': tk.BooleanVar(),
            'blue': tk.BooleanVar(),
            'sepia': tk.BooleanVar(),
            'black_and_white': tk.BooleanVar(),
            'invert': tk.BooleanVar(),
            'glitch': tk.BooleanVar(),
        }

        for filter_name, filter_var in self.filter_vars.items():
            checkbutton = tk.Checkbutton(self.root, text=filter_name.capitalize().replace('_', ' '), variable=filter_var)
            checkbutton.pack(anchor=tk.W)

        # Filter application options
        self.random_filters = tk.BooleanVar()
        self.check_random_filters = tk.Checkbutton(self.root, text="Apply filters at random intervals", variable=self.random_filters)
        self.check_random_filters.pack()

        self.apply_on_cuts = tk.BooleanVar()
        self.check_apply_on_cuts = tk.Checkbutton(self.root, text="Apply filters at cuts", variable=self.apply_on_cuts)
        self.check_apply_on_cuts.pack()

        self.combine_filters = tk.BooleanVar()
        self.check_combine_filters = tk.Checkbutton(self.root, text="Combine selected filters", variable=self.combine_filters)
        self.check_combine_filters.pack()

    def get_selected_filters(self):
        """Retrieve the selected filters."""
        return [filter_name for filter_name, filter_var in self.filter_vars.items() if filter_var.get()]

    def get_filter_options(self):
        """Retrieve the filter options."""
        return (
            self.random_filters.get(),
            self.apply_on_cuts.get(),
            self.combine_filters.get()
        )
