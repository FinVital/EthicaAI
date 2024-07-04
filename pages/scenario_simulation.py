import streamlit as st
from utils.ml import simulate_scenarios

def scenario_simulation():
    st.title("EthicaAI - Scenario Simulation")
    dilemma = st.session_state.get('dilemma', None)
    if dilemma:
        simulation_results = simulate_scenarios(dilemma)
        st.write("Simulation Results:")
        st.write(simulation_results)
    else:
        st.error("No dilemma submitted yet.")
