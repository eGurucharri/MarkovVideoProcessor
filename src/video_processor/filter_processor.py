import random
from moviepy.editor import concatenate_videoclips
from src.filters.filters import apply_single_filter, apply_random_filters

def apply_filters_on_cuts(clip, selected_filters, segment_times, combine_filters):
    """
    Aplica los filtros en los tiempos de corte definidos por los segmentos.
    Args:
        clip: El video clip completo.
        selected_filters: Lista de filtros seleccionados por el usuario.
        segment_times: Lista de tiempos de inicio y fin para cada segmento.
        combine_filters: Si se deben combinar múltiples filtros o no.
    Returns:
        Un nuevo clip con los filtros aplicados y los intervalos con los atributos de los filtros.
    """
    intervals = []
    for start_time, end_time in segment_times:
        segment = clip.subclip(start_time, end_time)
        attributes = []  # Para registrar los filtros aplicados a este segmento

        if combine_filters:
            # Si se combinan, aplicar varios filtros aleatoriamente
            segment, filters_applied = apply_random_filters(segment, selected_filters)
            attributes.append(f"filters_combined: {', '.join(filters_applied)}")
        else:
            # Aplicar un solo filtro aleatorio
            filter_type = random.choice(selected_filters)
            segment = apply_single_filter(segment, filter_type)
            attributes.append(f"filter: {filter_type}")

        intervals.append((segment, attributes))

    # Concatenar los clips con los filtros aplicados
    filtered_clips = [segment for segment, _ in intervals]
    return concatenate_videoclips(filtered_clips), intervals


def apply_filters_at_random_intervals(clip, selected_filters, total_duration, combine_filters):
    """
    Aplica filtros de manera aleatoria en intervalos de tiempo aleatorios.
    Args:
        clip: El video clip completo.
        selected_filters: Lista de filtros seleccionados por el usuario.
        total_duration: Duración total del video.
        combine_filters: Si se deben combinar múltiples filtros o no.
    Returns:
        Un nuevo clip con los filtros aplicados en intervalos aleatorios y los atributos de los filtros.
    """
    intervals = []
    current_time = 0
    while current_time < total_duration:
        # Define la duración aleatoria para cada intervalo
        interval_duration = random.uniform(1, 5)
        start_time = current_time
        end_time = min(current_time + interval_duration, total_duration)
        segment = clip.subclip(start_time, end_time)
        attributes = []  # Para registrar los filtros aplicados a este segmento

        if combine_filters:
            # Si se combinan, aplicar varios filtros aleatoriamente
            segment, filters_applied = apply_random_filters(segment, selected_filters)
            attributes.append(f"filters_combined: {', '.join(filters_applied)}")
        else:
            # Aplicar un solo filtro aleatorio
            filter_type = random.choice(selected_filters)
            segment = apply_single_filter(segment, filter_type)
            attributes.append(f"filter: {filter_type}")

        intervals.append((segment, attributes))
        current_time = end_time

    # Concatenar los clips con los filtros aplicados
    filtered_clips = [segment for segment, _ in intervals]
    return concatenate_videoclips(filtered_clips), intervals
