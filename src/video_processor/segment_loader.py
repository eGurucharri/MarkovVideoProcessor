from moviepy.editor import VideoFileClip
import os
import random

def load_videos(directory):
    """Carga los videos desde el directorio especificado."""
    video_clips = []
    for filename in os.listdir(directory):
        if filename.endswith(".mp4") or filename.endswith(".mov"):
            video_clips.append(VideoFileClip(os.path.join(directory, filename)))
    return video_clips

def get_random_segment(video_clip, min_duration, max_duration):
    """Obtiene un segmento aleatorio de un video, con duración mínima y máxima especificada."""
    total_duration = video_clip.duration
    start = random.uniform(0, total_duration - max_duration)
    end = min(start + random.uniform(min_duration, max_duration), total_duration)
    return video_clip.subclip(start, end)
