import ffmpeg
import os

def extract_audio(video_path, output_dir="audio"):
    os.makedirs(output_dir, exist_ok=True)
    audio_path = os.path.join(output_dir, "temp.wav")
    ffmpeg.input(video_path).output(audio_path, ac=1, ar='16k').run(overwrite_output=True)
    return audio_path
