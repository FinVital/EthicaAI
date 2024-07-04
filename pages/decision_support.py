import streamlit as st
from utils.openai_client import generate_insights
from utils.supabase_client import supabase

def decision_support():
    st.title("EthicaAI - Decision Support")
    
    dilemma = st.session_state.get('dilemma', None)
    if not dilemma:
        st.error("No dilemma submitted yet.")
        return

    # Generate insights using OpenAI
    insights = generate_insights(dilemma)

    st.write("Actionable Insights and Recommendations:")
    st.write(insights)

    # Option to save the decision process and outcomes
    if st.button("Save Decision Process"):
        decision_record = {
            "user_id": st.session_state['user']['id'],
            "dilemma": dilemma,
            "insights": insights
        }
        response = supabase.table('decision_records').insert(decision_record).execute()
        if response:
            st.success("Decision process saved successfully.")
        else:
            st.error("Failed to save decision process.")
