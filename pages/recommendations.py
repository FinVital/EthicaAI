import streamlit as st
from utils.ml import get_recommendations

def recommendations():
    st.title("EthicaAI - Recommendations")
    dilemma = st.session_state.get('dilemma', None)
    if dilemma:
        recommendations = get_recommendations(dilemma)
        st.write("Recommendations:", recommendations)
    else:
        st.error("No dilemma submitted yet.")
