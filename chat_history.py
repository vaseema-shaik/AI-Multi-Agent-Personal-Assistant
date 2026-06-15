import streamlit as st

def save_message(message):

    if "history" not in st.session_state:

        st.session_state.history = []

    st.session_state.history.append(
        message
    )

def show_history():

    if "history" in st.session_state:

        for msg in st.session_state.history:

            st.write(msg)