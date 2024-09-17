from src.filters.filters import apply_single_filter, apply_random_filters  # Importamos correctamente las funciones necesarias
from src.video_processor.segment_loader import load_videos, get_random_segment
from src.video_processor.filter_processor import apply_filters_on_cuts, apply_filters_at_random_intervals
from src.video_processor.video_saver import save_video
from src.logger.logger import TkProgressBarLogger
from src.utils.utils import update_status, get_unique_filename
from moviepy.editor import concatenate_videoclips, vfx
import random

def process_video(video_dir, total_duration, formats, progress_bar, status_text, selected_filters, base_name="output",
                  output_dir="./outputs/", use_random_filter_intervals=False, apply_on_cuts=False, combine_filters=False,
                  min_segment_duration=0.1, max_segment_duration=5.0, keep_original_speed=True,
                  slow_down=False, speed_up=False, reverse_speed=False, apply_filters_to_segments=False,
                  apply_one_filter_per_segment=False):
    """Proceso principal que selecciona segmentos aleatorios de los videos y permite cambios en la velocidad."""

    update_status(status_text, "Iniciando el procesamiento de los videos...")
    video_clips = load_videos(video_dir)

    if not video_clips:
        update_status(status_text, "Error: No se encontraron videos en la carpeta especificada.")
        return

    # Lista de posibles efectos de velocidad
    speed_effects = []
    if slow_down:
        speed_effects.append(("speed_halved", lambda segment: segment.fx(vfx.speedx, 0.5)))
    if speed_up:
        speed_effects.append(("speed_doubled", lambda segment: segment.fx(vfx.speedx, 2.0)))
    if reverse_speed:
        speed_effects.append(("speed_reversed", lambda segment: segment.fx(vfx.time_mirror)))

    all_segments = []
    segment_attributes = []
    current_duration = 0
    segment_times = []
    segment_counter = 1

    while current_duration < total_duration:
        selected_video = random.choice(video_clips)
        segment = get_random_segment(selected_video, min_segment_duration, max_segment_duration)
        segment_duration = segment.duration
        segment_label = f"segment_video_{segment_counter:02d}"
        segment_counter += 1
        attributes = []

        # Aplicar efectos de velocidad
        if not keep_original_speed and speed_effects:
            random_effect_name, random_effect = random.choice(speed_effects)
            segment = random_effect(segment)
            attributes.append(random_effect_name)

        # Aplicar filtros individualmente si está habilitada la opción y hay filtros seleccionados
        if apply_filters_to_segments and selected_filters:
            if apply_one_filter_per_segment:
                # Aplicar solo un filtro aleatorio de los seleccionados
                filter_type = random.choice(selected_filters)
                segment = apply_single_filter(segment, filter_type)
                attributes.append(f"filter: {filter_type}")
            else:
                # Aplicar múltiples filtros o combinarlos
                segment, filters_applied = apply_random_filters(segment, selected_filters)
                attributes.append(f"filters: {', '.join(filters_applied)}")

        if current_duration + segment_duration > total_duration:
            segment = segment.subclip(0, total_duration - current_duration)
            segment_duration = segment.duration

        all_segments.append(segment)
        segment_times.append((current_duration, current_duration + segment_duration))
        segment_attributes.append({
            "segment": segment_label,
            "duration": segment_duration,
            "attributes": attributes
        })

        current_duration += segment_duration
        update_status(status_text, f"Duración actual: {current_duration:.2f} segundos / {total_duration} segundos")

    final_clip = concatenate_videoclips(all_segments)

    # Aplicar filtros globalmente si no se aplica por segmento
    if not apply_filters_to_segments and selected_filters:
        if apply_on_cuts:
            update_status(status_text, "Aplicando filtros en los cortes...")
            final_clip, filtered_intervals = apply_filters_on_cuts(final_clip, selected_filters, segment_times, combine_filters)
        elif use_random_filter_intervals:  # Usar la nueva variable booleana correctamente
            update_status(status_text, "Aplicando filtros a intervalos aleatorios...")
            final_clip, filtered_intervals = apply_filters_at_random_intervals(final_clip, selected_filters, total_duration, combine_filters)

    # Guardar el video con progreso y ETA
    for fmt in formats:
        update_status(status_text, f"Guardando el video en formato {fmt}...")
        output_path = get_unique_filename(output_dir, base_name, fmt)
        logger = TkProgressBarLogger(progress_bar, status_text)
        save_video(final_clip, output_path, logger, fmt)

    # Mostrar los atributos de los segmentos
    for segment_data in segment_attributes:
        print(f"Segmento: {segment_data['segment']}, Duración: {segment_data['duration']}s, Atributos: {segment_data['attributes']}")
