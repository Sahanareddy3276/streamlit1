import streamlit as st

# Page configuration
st.set_page_config(page_title="Welcome Form", page_icon="📝", layout="centered")

# Custom CSS for improved UI
st.markdown("""
    <style>
        .main {
            background-color: #f0f8ff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            max-width: 600px;
            margin: auto;
        }
        h1, h3 {
            text-align: center;
            color: #2c3e50;
        }
        .stTextInput > div > div > input {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Main UI container
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown("## 👋 Welcome to My App")
    st.markdown("### Please enter your details below")

    # Input fields
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=1, max_value=120, step=1)

    # Display result after input
    if name and age:
        st.success(f"🎉 Welcome, **{name}**! You are **{age}** years old.")
    else:
        st.info("📝 Please fill in both fields to continue.")

    st.markdown('</div>', unsafe_allow_html=True)
