import streamlit as st
from utils.supabase_client import supabase

def dashboard():
    st.title("EthicaAI - Dashboard")
    
    try:
        # Fetch recent ethical dilemmas
        dilemmas_response = supabase.table('ethical_dilemmas').select('*').order('created_at', desc=True).limit(5).execute()
        dilemmas = dilemmas_response.data
        
        # Fetch saved scenarios
        scenarios_response = supabase.table('scenarios').select('*').order('created_at', desc=True).limit(5).execute()
        scenarios = scenarios_response.data
        
        # Fetch personalized recommendations
        recommendations_response = supabase.table('recommendations').select('*').order('created_at', desc=True).limit(5).execute()
        recommendations = recommendations_response.data
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return
    
    st.header("Recent Ethical Dilemmas")
    if dilemmas:
        for dilemma in dilemmas:
            with st.expander(dilemma['title']):
                st.write(dilemma['description'])
                if st.button(f"View Details of {dilemma['title']}", key=f"view_{dilemma['id']}"):
                    st.session_state['dilemma'] = dilemma
                    st.experimental_rerun()
    else:
        st.write("No recent ethical dilemmas found.")
    
    st.header("Saved Scenarios")
    if scenarios:
        for scenario in scenarios:
            with st.expander(scenario['title']):
                st.write(scenario['description'])
                if st.button(f"View {scenario['title']}", key=f"view_scenario_{scenario['id']}"):
                    st.session_state['scenario'] = scenario
                    st.experimental_rerun()
                if st.button(f"Delete {scenario['title']}", key=f"delete_scenario_{scenario['id']}"):
                    supabase.table('scenarios').delete().eq('id', scenario['id']).execute()
                    st.success(f"Deleted scenario: {scenario['title']}")
                    st.experimental_rerun()
    else:
        st.write("No saved scenarios found.")
    
    st.header("Personalized Recommendations")
    if recommendations:
        for recommendation in recommendations:
            st.write(recommendation['text'])
    else:
        st.write("No personalized recommendations found.")
    
    st.header("Navigate to Other Sections")
    if st.button("Input Ethical Dilemma"):
        st.session_state['page'] = "Ethical Dilemma Input"
        st.experimental_rerun()
    
    if st.button("Perform Ethical Analysis"):
        st.session_state['page'] = "Ethical Analysis"
        st.experimental_rerun()
    
    if st.button("Simulate Scenarios"):
        st.session_state['page'] = "Scenario Simulation"
        st.experimental_rerun()
    
    if st.button("Get Recommendations"):
        st.session_state['page'] = "Recommendations"
        st.experimental_rerun()

    if st.button("Decision Support"):
        st.session_state['page'] = "Decision Support"
        st.experimental_rerun()
