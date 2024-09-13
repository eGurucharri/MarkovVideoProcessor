from src.video_processor.segment_loader import load_videos, get_random_segment
from src.video_processor.filter_processor import apply_filters_on_cuts, apply_filters_at_random_intervals, \
    apply_filters_continuously
from src.video_processor.video_saver import save_video
from src.logger.logger import TkProgressBarLogger
from src.utils.utils import update_status, get_unique_filename
from moviepy.editor import concatenate_videoclips
import random


def process_video(video_dir, total_duration, formats, progress_bar, status_text, selected_filters, base_name="output",
                  output_dir="./outputs/", apply_random_filters=False, apply_on_cuts=False, combine_filters=False,
                  min_segment_duration=0.1, max_segment_duration=5.0):
    """Proceso principal que selecciona segmentos aleatorios de los videos hasta completar la duración total deseada."""

    update_status(status_text, "Iniciando el procesamiento de los videos...")
    video_clips = load_videos(video_dir)

    if not video_clips:
        update_status(status_text, "Error: No se encontraron videos en la carpeta especificada.")
        return

    all_segments = []
    current_duration = 0
    segment_times = []

    while current_duration < total_duration:
        selected_video = random.choice(video_clips)
        segment = get_random_segment(selected_video, min_segment_duration, max_segment_duration)
        segment_duration = segment.duration
        if current_duration + segment_duration > total_duration:
            segment = segment.subclip(0, total_duration - current_duration)
            segment_duration = segment.duration

        all_segments.append(segment)
        segment_times.append((current_duration, current_duration + segment_duration))
        current_duration += segment_duration
        update_status(status_text, f"Duración actual: {current_duration:.2f} segundos / {total_duration} segundos")

    final_clip = concatenate_videoclips(all_segments)

    # Aplicar los filtros si hay seleccionados
    if selected_filters:
        if apply_on_cuts:
            update_status(status_text, "Aplicando filtros en los cortes...")
            final_clip = apply_filters_on_cuts(final_clip, selected_filters, segment_times, combine_filters)
        elif apply_random_filters:
            update_status(status_text, "Aplicando filtros a intervalos aleatorios...")
            final_clip = apply_filters_at_random_intervals(final_clip, selected_filters, total_duration,
                                                           combine_filters)
        else:
            update_status(status_text, "Aplicando filtros seleccionados continuamente...")
            final_clip = apply_filters_continuously(final_clip, selected_filters, combine_filters)
    else:
        update_status(status_text, "No se aplicaron filtros.")

    # Guardar el video con progreso y ETA
    for fmt in formats:
        update_status(status_text, f"Guardando el video en formato {fmt}...")
        output_path = get_unique_filename(output_dir, base_name, fmt)
        logger = TkProgressBarLogger(progress_bar, status_text)
        save_video(final_clip, output_path, logger, fmt)
