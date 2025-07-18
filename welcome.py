import streamlit as st
st.set_page_config(page_title="Simple Streamlit App", layout="centered")
st.title("📘 Welcome to My Streamlit App")
st.header("Simple Form Example")
st.write("This is a basic example of using Streamlit in Python.")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=120, step=1)

if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old!")
