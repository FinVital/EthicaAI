import streamlit as st
from utils.auth import register

def register():
    st.title("EthicaAI - Register")
    register()
    st.markdown("[Back to Login](#)")
