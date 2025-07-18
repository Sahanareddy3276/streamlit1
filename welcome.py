import streamlit as st

# Page config
st.set_page_config(page_title="User Info Form", layout="centered")

# Inject CSS for better styling
st.markdown("""
    <style>
        .main-container {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 3rem 2rem;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            margin: auto;
        }
        h1 {
            text-align: center;
            color: #222;
            font-family: 'Segoe UI', sans-serif;
            font-size: 2.2rem;
        }
        label {
            font-weight: 600;
            font-size: 1rem;
            color: #333;
        }
        .stTextInput > div > div > input, 
        .stNumberInput > div > div > input {
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title
st.markdown("<h1>Welcome</h1>", unsafe_allow_html=True)
st.markdown("### Please enter your details below")

# User Inputs
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120, step=1)

# Display after input
if name and age:
    st.markdown("---")
    st.markdown(f"**Hello {name},** you are **{int(age)}** years old.")

st.markdown("</div>", unsafe_allow_html=True)
