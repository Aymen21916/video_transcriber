import time
start_time = time.time()

from app.extractor import extract_audio
from app.transcriber import transcribe_audio
from app.question_detector import detect_questions_llm
from app.answer_questions import answer_question

video_path = "videos\\video_path.mp4"

# Step 1: Extract audio
audio_path = extract_audio(video_path)

# Step 2: Transcribe audio
transcription = transcribe_audio(audio_path)
print("=== Transcription ===")
print(transcription)

# Step 3: Detect questions
questions = detect_questions_llm(transcription)
print("\n=== Detected Questions ===")
for q in questions: 
    print("-", q)

# Step 4: Answer questions
for q in questions:
    answer = answer_question(q)
    print(f"- {q} \n", answer, "\n")
    print("<==============================================================================================================================================================================>")

end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")