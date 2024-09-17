from moviepy.editor import vfx
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
        return clip.fx(vfx.blackwhite)
    return clip

def apply_aberrant_color_filter(clip, filter_type):
    """Aplica filtros aberrantes o distorsionados al clip."""
    if filter_type == 'invert':
        return clip.fx(vfx.invert_colors)
    elif filter_type == 'glitch':
        return clip.fl_image(lambda image: image * [2, 1.5, 2.5])
    return clip

def apply_single_filter(clip, filter_type):
    """Aplica un solo filtro al clip basado en el tipo de filtro."""
    if filter_type in ['red', 'green', 'blue']:
        return apply_basic_color_filter(clip, filter_type)
    elif filter_type in ['sepia', 'black_and_white']:
        return apply_natural_color_filter(clip, filter_type)
    elif filter_type in ['invert', 'glitch']:
        return apply_aberrant_color_filter(clip, filter_type)
    return clip

def apply_random_filters(clip, selected_filters):
    """Selecciona uno o más filtros de manera aleatoria y los aplica al clip."""
    # Seleccionar uno o más filtros aleatoriamente
    filters_to_apply = random.sample(selected_filters, k=random.randint(1, len(selected_filters)))

    # Aplicar los filtros seleccionados al clip
    for filter_type in filters_to_apply:
        clip = apply_single_filter(clip, filter_type)

    return clip, filters_to_apply  # Devolver los filtros aplicados para registro
