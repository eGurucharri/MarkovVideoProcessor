import os
from src.video_processor.video_processor import process_video
from src.video_processor.segment_loader import get_random_segment  # Importar get_random_segment
from moviepy.editor import VideoFileClip

def test_process_video_without_filters():
    process_video(
        video_dir="./videos/",
        total_duration=10,
        formats=[".mp4"],
        progress_bar=None,
        status_text=None,
        selected_filters=[],
        base_name="test_output",
        apply_random_filters=False,
        apply_on_cuts=False,
        combine_filters=False,
        min_segment_duration=0.5,
        max_segment_duration=3.0,
    )
    assert os.path.exists("./outputs/test_output.mp4")

def test_video_segment_duration():
    clip = VideoFileClip("path/to/sample.mp4")
    segment = get_random_segment(clip, 1.0, 5.0)
    assert 1.0 <= segment.duration <= 5.0
