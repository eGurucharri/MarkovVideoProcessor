import os

def update_status(status_text, message):
    """Función para actualizar el cuadro de estado en la UI."""
    status_text.insert('end', message + '\n')
    status_text.see('end')
    status_text.update_idletasks()

def get_unique_filename(directory, base_name, extension):
    """Devuelve un nombre de archivo único añadiendo un número si ya existe."""
    full_path = os.path.join(directory, f"{base_name}{extension}")
    counter = 1
    while os.path.exists(full_path):
        full_path = os.path.join(directory, f"{base_name}_{counter}{extension}")
        counter += 1
    return full_path

