import random
from moviepy.editor import concatenate_videoclips
from src.filters.filters import apply_single_filter

def apply_filters_on_cuts(clip, selected_filters, segment_times, combine_filters):
    """Aplica los filtros en los tiempos de corte, opcionalmente combinándolos."""
    intervals = []
    for start_time, end_time in segment_times:
        segment = clip.subclip(start_time, end_time)
        if combine_filters:
            for filter_type in selected_filters:
                segment = apply_single_filter(segment, filter_type)
        else:
            filter_type = random.choice(selected_filters)
            segment = apply_single_filter(segment, filter_type)
        intervals.append(segment)
    return concatenate_videoclips(intervals)

def apply_filters_at_random_intervals(clip, selected_filters, total_duration, combine_filters):
    """Aplica filtros de manera aleatoria en intervalos."""
    intervals = []
    current_time = 0
    while current_time < total_duration:
        interval_duration = random.uniform(1, 5)
        start_time = current_time
        end_time = min(current_time + interval_duration, total_duration)
        segment = clip.subclip(start_time, end_time)
        if combine_filters:
            for filter_type in selected_filters:
                segment = apply_single_filter(segment, filter_type)
        else:
            filter_type = random.choice(selected_filters)
            segment = apply_single_filter(segment, filter_type)
        intervals.append(segment)
        current_time = end_time
    return concatenate_videoclips(intervals)

def apply_filters_continuously(clip, selected_filters, combine_filters):
    """Aplica los filtros seleccionados de manera continua al clip."""
    if combine_filters:
        for filter_type in selected_filters:
            clip = apply_single_filter(clip, filter_type)
    else:
        filter_type = random.choice(selected_filters)
        clip = apply_single_filter(clip, filter_type)
    return clip
