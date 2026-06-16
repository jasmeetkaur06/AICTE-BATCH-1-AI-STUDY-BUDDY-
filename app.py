import streamlit as st
from groq import Groq

def call_ai(prompt):
    try:
        api_key = st.secrets.get("GROQ_API_KEY", "")
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

st.set_page_config(page_title="AI Study Buddy", page_icon="📚", layout="centered")

with st.sidebar:
    st.title("📚 AI Study Buddy")
    st.markdown("---")
    st.markdown("**Features:**")
    st.markdown("- Explain any topic simply")
    st.markdown("- Summarize notes")
    st.markdown("- Generate MCQ quiz")
    st.markdown("- Create flashcards")
    st.markdown("---")
    st.caption("EduNet IBM SkillsBuild AICTE")

st.title("AI Study Buddy")
st.markdown("Your personal AI-powered learning assistant powered by **Groq + LLaMA 3.1**")
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["Explain Topic", "Summarize Notes", "Generate Quiz", "Flashcards"])

with tab1:
    st.subheader("Explain any topic in simple terms")
    topic = st.text_input("Enter a topic", placeholder="e.g. Photosynthesis, Newton Laws, Binary Search")
    level = st.selectbox("Level", ["Beginner", "Student Class 10-12", "College level"])
    if st.button("Explain This Topic", key="b1"):
        if not topic.strip():
            st.warning("Please enter a topic.")
        else:
            with st.spinner("Generating explanation..."):
                prompt = f"""Explain "{topic}" at level: {level}.
1. Simple Definition (2-3 sentences)
2. How It Works (with a simple analogy)
3. Key Points (4-5 bullet points)
4. Real-life Example (1 short example)"""
                st.markdown(call_ai(prompt))

with tab2:
    st.subheader("Summarize your study notes")
    notes = st.text_area("Paste your notes here", height=220,
        placeholder="Paste textbook text or lecture notes here...")
    c1, c2 = st.columns(2)
    with c1:
        style = st.selectbox("Style", ["Bullet points", "Short paragraph", "Key terms only"])
    with c2:
        length = st.selectbox("Length", ["Short", "Medium", "Detailed"])
    if st.button("Summarize My Notes", key="b2"):
        if not notes.strip():
            st.warning("Please paste some notes.")
        else:
            with st.spinner("Summarizing..."):
                prompt = f"""Summarize these study notes.
Style: {style} | Length: {length}
Notes:
{notes}
Make it clear and useful for exam revision."""
                st.markdown(call_ai(prompt))

with tab3:
    st.subheader("Test your knowledge with a quiz")
    quiz_topic = st.text_input("Quiz topic", placeholder="e.g. World War 2, Python, Solar System")
    difficulty = st.select_slider("Difficulty", options=["Easy", "Medium", "Hard"], value="Medium")
    if st.button("Generate Quiz", key="b3"):
        if not quiz_topic.strip():
            st.warning("Please enter a topic.")
        else:
            with st.spinner("Creating 5 quiz questions..."):
                prompt = f"""Create a quiz on "{quiz_topic}", difficulty: {difficulty}.
Generate exactly 5 MCQs:

Q1. [Question]
A) [Option]
B) [Option]
C) [Option]
D) [Option]
Answer: [Letter]
Explanation: [One sentence]

Repeat for Q2 to Q5."""
                st.markdown(call_ai(prompt))
                st.success("Quiz ready!")

with tab4:
    st.subheader("Generate flashcards for quick revision")
    flash_topic = st.text_input("Flashcard topic", placeholder="e.g. Python data types, Periodic table")
    num_cards = st.slider("Number of flashcards", 3, 10, 5)
    if st.button("Generate Flashcards", key="b4"):
        if not flash_topic.strip():
            st.warning("Please enter a topic.")
        else:
            with st.spinner("Creating flashcards..."):
                prompt = f"""Create {num_cards} flashcards on "{flash_topic}".

Card [number]
Q: [Question]
A: [Answer in 1-3 sentences]

Leave a blank line between cards."""
                st.markdown(call_ai(prompt))
                st.success(f"{num_cards} flashcards ready!")
