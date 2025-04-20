import streamlit as st
from prompts import job_prompts
from utils import get_openai_response
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Interview Coach", layout="centered")
st.title("🤖 AI Interview Coach")

job_role = st.selectbox("Choose your job role:", list(job_prompts.keys()))

if st.button("Generate Interview Questions"):
    prompt = job_prompts[job_role]
    question = get_openai_response(prompt)
    st.markdown("### 🗣️ Interview Questions")
    st.write(question)

    user_answer = st.text_area("✍️ Write your answer here:")
    
    if st.button("Submit Answer for Feedback"):
        feedback_prompt = f"Evaluate this interview answer and give me feedback with pros and cons:\n\n{user_answer}"
        feedback = get_openai_response(feedback_prompt)
        st.markdown("### 📋 Feedback from AI")
        st.write(feedback)