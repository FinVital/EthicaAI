import streamlit as st
from utils.auth import login, guest_login

def login():
    st.title("EthicaAI - Login")
    
    st.markdown("## Existing Users")
    login()

    st.markdown("## New Users")
    st.markdown("[Go to Register Page](#)")

    st.markdown("## Guest Access")
    if st.button("Guest Mode"):
        guest_login()
