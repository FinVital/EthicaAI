import streamlit as st
import pages.dashboard as dashboard
import pages.ethical_dilemma_input as ethical_dilemma_input
import pages.ethical_analysis as ethical_analysis
import pages.scenario_simulation as scenario_simulation
import pages.recommendations as recommendations
import pages.decision_support as decision_support

st.set_page_config(page_title="EthicaAI")

# Initialize session state
if 'page' not in st.session_state:
    st.session_state['page'] = 'Dashboard'

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Ethical Dilemma Input", "Ethical Analysis", "Scenario Simulation", "Recommendations", "Decision Support"])

if page:
    st.session_state['page'] = page

# Page navigation
if st.session_state['page'] == "Dashboard":
    dashboard.dashboard()
elif st.session_state['page'] == "Ethical Dilemma Input":
    ethical_dilemma_input.ethical_dilemma_input()
elif st.session_state['page'] == "Ethical Analysis":
    ethical_analysis.ethical_analysis()
elif st.session_state['page'] == "Scenario Simulation":
    scenario_simulation.scenario_simulation()
elif st.session_state['page'] == "Recommendations":
    recommendations.recommendations()
elif st.session_state['page'] == "Decision Support":
    decision_support.decision_support()
