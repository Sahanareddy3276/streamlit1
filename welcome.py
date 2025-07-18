import streamlit as st

# Page configuration
st.set_page_config(page_title="Welcome Page", page_icon="👋", layout="centered")

# Welcome message
st.title("👋 Welcome to My Streamlit App!")
st.subheader("We're glad you're here, Sahana!")

# Optional description
st.markdown("""
### Explore the App
This simple app displays your picture and a welcome message using Streamlit.

✨ Feel free to customize it further with buttons, inputs, or color themes!
""")
