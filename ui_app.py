import streamlit as st
from narration_generator import generate_narration
from gtts import gTTS

st.title("🎙️ Contextual Narration Generator")
st.write("Generate personalized narrations for various occasions and topics.")

with st.form("input_form"):
    occasion = st.text_input("Occasion (e.g., Birthday, Farewell)")
    topic = st.text_input("Topic (e.g., Friendship, AI, Dreams)")
    tone = st.selectbox("Tone", ["Formal", "Emotional", "Inspirational", "Funny"])
    audience = st.text_input("Audience (e.g., College Friends, Students)")
    length = st.selectbox("Length", ["Short", "Medium", "Long"])

    submitted = st.form_submit_button("Generate Narration")

if submitted:
    user_input = {
        "occasion": occasion,
        "topic": topic,
        "tone": tone,
        "audience": audience,
        "length": length
    }

    with st.spinner("Generating..."):
        narration = generate_narration(occasion, topic,length)


    st.subheader("📝 Generated Narration:")
    st.write(narration)

    tts = gTTS(text=narration)
    tts.save("output.mp3")
    st.audio("output.mp3", format="audio/mp3")