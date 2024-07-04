import streamlit as st
from utils.supabase_client import supabase

def guest_login():
    st.title("EthicaAI - Guest Mode")
    if st.button("Enter as Guest"):
        st.session_state['user'] = "guest"
        st.experimental_rerun()
