import streamlit as st

# ---- SETUP ----
st.set_page_config(page_title="Joshua Del Rosario", page_icon="🥶", layout="centered")

# ---- HEADER SECTION ----
with st.container():
    st.title("Hello! 🌃")
    st.write("##### My name is Joshua Del Rosario.")
    st.image("chicago photo.jpg")

with st.container():
    st.subheader("About Me")
    st.write("""
    - I am a freshman at the University of Illinois Chicago: majoring in computer science, minoring in math.
    - I am an aspiring full-stack developer and wish to work in web development and machine learning.
    - I have experience with Python, Arduino, and C++.
    """)
    st.write("[Linkedin](https://www.linkedin.com/in/joshua-del-rosario-03b648298/) "
             "[Github](https://github.com/jvdrosario)")

with st.container():
    st.subheader("Projects")
    st.image("Screenshot 2024-02-07 133039.png", width=500)
    st.write("##### [Budgeting Financial App](https://github.com/jvdrosario/turtle-budgeting-app) ")
    st.write("""
    - Developed user-interface with Python’s Turtle library
    - Create budgets and report expenses in user-created categories
    - Able to save and retrieve user’s data upon closing the app, using .txt files
    - Able to calculate monthly savings and expenses for user and prioritize this spending
    - Displays pie graph of expenditure that automatically updates after every transaction
    - Utilized Python and Turtle library
    """)
