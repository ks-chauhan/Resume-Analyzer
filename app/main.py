import streamlit as st
import shortlist
import single_score
import home

## Set the page configuration
st.set_page_config(page_title="Resume Analyzer")

# Sidebar to navigate between pages
st.sidebar.title("Navigator")
selection = st.sidebar.radio("Go to", ["Home", "Single Resume Analysis", "Resume Shortlist"])

if selection == "Home":
    home.Main()
elif selection == "Single Resume Analysis":
    single_score.Main()
elif selection == "Resume Shortlist":
    shortlist.Main()