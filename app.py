import streamlit as st
from utils.auth import login, register, guest_login
import pages.dashboard as dashboard
import pages.ethical_dilemma_input as ethical_dilemma_input
import pages.ethical_analysis as ethical_analysis
import pages.scenario_simulation as scenario_simulation
import pages.recommendations as recommendations
import pages.decision_support as decision_support
import pages.register as register_page

st.set_page_config(page_title="EthicaAI")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Ethical Dilemma Input", "Ethical Analysis", "Scenario Simulation", "Recommendations", "Decision Support"])

if page == "Dashboard":
    dashboard.dashboard()
elif page == "Ethical Dilemma Input":
    ethical_dilemma_input.ethical_dilemma_input()
elif page == "Ethical Analysis":
    ethical_analysis.ethical_analysis()
elif page == "Scenario Simulation":
    scenario_simulation.scenario_simulation()
elif page == "Recommendations":
    recommendations.recommendations()
elif page == "Decision Support":
    decision_support.decision_support()
