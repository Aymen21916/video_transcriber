from app.extractor import extract_audio
from app.transcriber import transcribe_audio

video_path = "videos/sample.mp4"

# Step 1: Extract audio
audio_path = extract_audio(video_path)

# Step 2: Transcribe audio
transcription = transcribe_audio(audio_path)

# Step 3: Print result
print("=== Transcription ===")
print(transcription)
