from moviepy.editor import VideoFileClip
from src.filters.filters import apply_basic_color_filter

def test_apply_red_filter():
    clip = VideoFileClip("../videos/sample.mp4").subclip(0, 5)
    filtered_clip = apply_basic_color_filter(clip, 'red')
    assert filtered_clip is not None
