import streamlit as st
from utils.ml import analyze_dilemma

def ethical_analysis():
    st.title("EthicaAI - Ethical Analysis")
    dilemma = st.session_state.get('dilemma', None)
    if dilemma:
        analysis = analyze_dilemma(dilemma)
        st.write("Ethical Implications:", analysis)
    else:
        st.error("No dilemma submitted yet.")
