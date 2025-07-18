import streamlit as st

# Page config
st.set_page_config(page_title="User Info Form", layout="centered")

# Custom CSS for stylish UI
st.markdown("""
    <style>
        body {
            background-color: #e6f0f8;
        }
        .main-container {
            background-color: #ffffff;
            padding: 3rem 2rem;
            border-radius: 16px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            margin: 3rem auto;
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            color: #1a1a1a;
            text-align: center;
            margin-bottom: 1.5rem;
        }
        .stTextInput > div > div > input, 
        .stNumberInput > div > div > input {
            background-color: #f5f7fa;
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 10px;
        }
        .stMarkdown {
            font-size: 1rem;
            color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title and subtitle
st.markdown("<h1>Welcome to the Portal</h1>", unsafe_allow_html=True)
st.markdown("Please fill in the details below:")

# Input fields
name = st.text_input("Your Name")
age = st.number_input("Your Age", min_value=1, max_value=120, step=1)

# Display message after input
if name and age:
    st.markdown("---")
    st.markdown(f"Hello, **{name}**. You are **{int(age)}** years old.")

st.markdown('</div>', unsafe_allow_html=True)
