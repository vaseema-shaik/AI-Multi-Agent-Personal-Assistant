import streamlit as st

def login():

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        st.success(
            f"Welcome {username}"
        )