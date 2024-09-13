import os
from src.utils.utils import get_unique_filename

def test_get_unique_filename():
    filename = get_unique_filename("./outputs/", "output", ".mp4")
    assert filename.startswith("output")
    assert filename.endswith(".mp4")
