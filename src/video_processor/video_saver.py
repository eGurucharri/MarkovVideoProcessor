def save_video(final_clip, output_path, logger, video_format=".mp4"):
    """Guarda el video final con el nombre único."""
    final_clip.write_videofile(output_path, codec='libx264', preset='fast', bitrate="5000k", logger=logger)
