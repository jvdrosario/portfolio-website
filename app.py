import streamlit as st

# ---- SETUP ----
st.set_page_config(page_title="Joshua Del Rosario", page_icon="🥶", layout="centered")

# ---- HEADER SECTION ----
with st.container():
    st.title("Hello! 🌃")
    st.write("##### My name is Joshua Del Rosario.")
    st.image("chicago photo.jpg")

with st.container():
    st.write("""
    ### About Me
    - I am a freshman at the University of Illinois Chicago: majoring in computer science, minoring in math.
    - I am an aspiring full-stack developer and wish to work in web development and machine learning.
    - I have experience with Python, Arduino, and C++.
    """)
    st.write("[Linkedin](https://www.linkedin.com/in/joshua-del-rosario-03b648298/) "
             "[Github](https://github.com/jvdrosario)")
