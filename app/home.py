import streamlit as st


## Simple Home Page to detail what the app does
def Main():
    """
    Home Page
    """
    st.title("Welcome to the Resume Analyzer App")
    st.markdown("""
    ### What this app does:
    - Score a Single Resume against a Job Description.
    - Shortlist Multiple Resumes based on a Job Description.
    
    ### How to use:
    - Navigate to the 'Single Resume Analysis' page to analyze one resume at a time.
    - Navigate to the 'Resume Shortlist' page to upload and shortlist multiple resumes.
    
    """)
