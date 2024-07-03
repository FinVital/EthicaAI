import streamlit as st
from utils.supabase_client import supabase

def login():
    st.title("EthicaAI - Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        user = supabase.auth.sign_in(email=username, password=password)
        if user:
            st.session_state['user'] = user
            st.success("Login successful")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")

def register():
    st.title("EthicaAI - Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Register"):
        user = supabase.auth.sign_up(email=username, password=password)
        if user:
            st.session_state['user'] = user
            st.success("Registration successful")
            st.experimental_rerun()
        else:
            st.error("Registration failed")

def guest_login():
    st.title("EthicaAI - Guest Mode")
    if st.button("Enter as Guest"):
        st.session_state['user'] = "guest"
        st.experimental_rerun()
