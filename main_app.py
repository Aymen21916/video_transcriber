import streamlit as st
from app.extractor import extract_audio
from app.transcriber import transcribe_audio
from app.question_detector import detect_questions_llm
from app.answer_questions import answer_question

st.title("🎥 Video Q&A App (Powered By Gemini)")

uploaded_video = st.file_uploader("Upload a video file", type=["mp4", "mov", "mkv"])

if uploaded_video is not None:
    # Save the uploaded video temporarily
    video_path = f"videos/{uploaded_video.name}"
    with open(video_path, "wb") as f:
        f.write(uploaded_video.getbuffer())
    st.success("✅ Video uploaded!")

    if st.button("Process Video"):
        with st.spinner("Extracting audio..."):
            audio_path = extract_audio(video_path)

        with st.spinner("Transcribing video..."):
            transcription = transcribe_audio(audio_path)
            st.text_area("Transcript:", transcription, height=400)

        with st.spinner("Detecting questions..."):
            questions = detect_questions_llm(transcription)
            st.write(f"✅ Found {len(questions)} questions.")
            for q in questions:
                st.write(f"**Q:** {q}")

        with st.spinner("Answering questions with Gemini..."):
            for q in questions:
                ans = answer_question(q)
                st.markdown(f"**Q:** {q}\n\n✅ **A:** {ans}\n---")
