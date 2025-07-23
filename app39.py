import streamlit as st
import time
import random

# Page Configuration
st.set_page_config(page_title="Typing Speed Tester", layout="centered")

st.title("🖋️ Typing Speed Tester")

# Sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Streamlit makes it easy to build web apps in Python.",
    "Typing speed is measured in words per minute.",
    "Practice makes perfect when it comes to typing speed."
]
sentence = random.choice(sentences)

# Display sentence
st.subheader("Type the following sentence:")
st.code(sentence)

# Start button
if "start_time" not in st.session_state:
    st.session_state.start_time = None

if st.button("Start Typing"):
    st.session_state.start_time = time.time()

# Typing input
user_input = st.text_area("Start Typing Here:")

# Submit button
if st.button("Submit"):
    if st.session_state.start_time:
        time_taken = time.time() - st.session_state.start_time
        words = len(sentence.split())
        speed = (words / time_taken) * 60 if time_taken > 0 else 0
        accuracy = "✅ Perfect!" if user_input.strip() == sentence else "❌ Try Again"

        st.write(f"**Your Speed:** {speed:.2f} WPM")
        st.write(f"**Accuracy:** {accuracy}")
    else:
        st.warning("⚠️ Please click 'Start Typing' first!")

