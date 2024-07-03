import streamlit as st

def ethical_dilemma_input():
    st.title("EthicaAI - Ethical Dilemma Input")
    context = st.text_area("Context of the ethical dilemma")
    stakeholders = st.text_input("Stakeholders involved")
    decisions = st.text_area("Potential decisions")
    ethical_theories = st.text_input("Relevant ethical theories")
    cultural_norms = st.text_input("Relevant cultural norms")
    if st.button("Submit"):
        dilemma = {
            "context": context,
            "stakeholders": stakeholders,
            "decisions": decisions,
            "ethical_theories": ethical_theories,
            "cultural_norms": cultural_norms
        }
        st.session_state['dilemma'] = dilemma
        st.success("Dilemma submitted successfully")
