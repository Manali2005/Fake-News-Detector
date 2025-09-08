import streamlit as st
import joblib

# Load model and vectorizer
vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("lr_model.jb")

# Page config
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Elegant Dark Theme
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #f5f5f5;
    }
    .title {
        font-size:42px;
        color:#FFD700; /* Gold */
        text-align:center;
        font-weight:800;
    }
    .subtitle {
        font-size:18px;
        text-align:center;
        color:#C0C0C0; /* Silver */
        margin-bottom:25px;
    }
    .stTextArea textarea {
        background-color: #111111;
        color: #ffffff;
        border: 1.5px solid #FFD700;
        border-radius: 10px;
        font-size: 16px;
    }
    .stButton button {
        background-color: #FFD700;
        color: black;
        border-radius: 10px;
        font-size: 18px;
        font-weight: 600;
        height: 3em;
        width: 100%;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #C0C0C0;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Subtitle
st.markdown("<div class='title'>📰 Fake News Detector</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Check if a news article is Real ✅ or Fake ❌</div>", unsafe_allow_html=True)

# Input box
inputn = st.text_area("✍️ Paste your news article here:", "", height=180)

# Detect button
if st.button("🔍 Detect"):
    if inputn.strip():
        transform_input = vectorizer.transform([inputn])
        prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.success("✅ The News is Real!")
        else:
            st.error("❌ The News is Fake!")
    else:
        st.warning("⚠️ Please enter some text to analyze.")
