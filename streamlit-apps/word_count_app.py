import streamlit as st

def count_words(sentence):
    words = sentence.strip().split(" ")
    st.markdown("### Words in your sentence:")
    st.write(words)
    st.markdown(f"### Your sentence word count is: **{len(words)}**")

st.title("🌈 Word Count Application 🌈")
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    h1 {
        color: #ff6347;
        text-align: center;
    }
    h2, h3 {
        color: #4682b4;
    }
    .stTextInput > div > div > input {
        background-color: #e6e6fa;
        border: 2px solid #4682b4;
        border-radius: 5px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.header("Enter your sentence below to count the words:")

if 'history' not in st.session_state:
    st.session_state.history = []

sentence = st.text_input("Sentence:")
if sentence:
    st.session_state.history.append(sentence)
    count_words(sentence)

if st.button("Clear History"):
    st.session_state.history = []

if st.session_state.history:
    st.markdown("### History:")
    for i, s in enumerate(st.session_state.history, 1):
        st.write(f"{i}. {s}")