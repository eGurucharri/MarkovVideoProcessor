from moviepy.editor import concatenate_videoclips
from moviepy.video.fx.all import invert_colors, blackwhite  # Estas sí existen en moviepy.video.fx
import random

def apply_basic_color_filter(clip, color):
    """Aplica un filtro de color básico al clip ajustando brillo y saturación manualmente."""
    if color == 'red':
        return clip.fl_image(lambda image: image * [1.5, 0.5, 0.5])
    elif color == 'green':
        return clip.fl_image(lambda image: image * [0.5, 1.5, 0.5])
    elif color == 'blue':
        return clip.fl_image(lambda image: image * [0.5, 0.5, 1.5])
    return clip

def apply_natural_color_filter(clip, filter_type):
    """Aplica filtros de colores naturales."""
    if filter_type == 'sepia':
        return clip.fl_image(lambda image: image * [1.1, 0.9, 0.8])
    elif filter_type == 'black_and_white':
        return blackwhite(clip)  # Blanco y negro
    return clip

def apply_aberrant_color_filter(clip, filter_type):
    """Aplica filtros aberrantes o distorsionados al clip."""
    if filter_type == 'invert':
        return invert_colors(clip)
    elif filter_type == 'glitch':
        return clip.fl_image(lambda image: image * [2, 1.5, 2.5])
    return clip

def apply_single_filter(clip, filter_type):
    """Aplica un solo filtro al clip basado en el tipo de filtro."""
    if filter_type == 'red':
        return apply_basic_color_filter(clip, 'red')
    elif filter_type == 'green':
        return apply_basic_color_filter(clip, 'green')
    elif filter_type == 'blue':
        return apply_basic_color_filter(clip, 'blue')
    elif filter_type == 'sepia':
        return apply_natural_color_filter(clip, 'sepia')
    elif filter_type == 'black_and_white':
        return apply_natural_color_filter(clip, 'black_and_white')
    elif filter_type == 'invert':
        return apply_aberrant_color_filter(clip, 'invert')
    elif filter_type == 'glitch':
        return apply_aberrant_color_filter(clip, 'glitch')
    return clip

def apply_combined_filters(clip, selected_filters):
    """Combina todos los filtros seleccionados y los aplica al clip."""
    for filter_type in selected_filters:
        clip = apply_single_filter(clip, filter_type)
    return clip

def apply_filters_at_random_intervals(clip, selected_filters, total_duration, combine_filters=False):
    """Aplica filtros de manera aleatoria en intervalos, combinando filtros solo si está seleccionado."""
    intervals = []
    current_time = 0

    while current_time < total_duration:
        # Define la duración aleatoria para cada intervalo
        interval_duration = random.uniform(1, 5)
        start_time = current_time
        end_time = min(current_time + interval_duration, total_duration)

        # Seleccionar y aplicar los filtros según si se deben combinar o no
        filtered_clip = clip.subclip(start_time, end_time)
        if combine_filters:
            filtered_clip = apply_combined_filters(filtered_clip, selected_filters)
        else:
            # Solo aplicar un filtro si no se deben combinar
            filter_type = random.choice(selected_filters)
            filtered_clip = apply_single_filter(filtered_clip, filter_type)

        intervals.append(filtered_clip)
        current_time = end_time

    return concatenate_videoclips(intervals)
