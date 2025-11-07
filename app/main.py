import streamlit as st
import shortlist
import single_score
import home


st.set_page_config(page_title="Resume Analyzer")

st.sidebar.title("Navigator")
selection = st.sidebar.radio("Go to", ["Home", "Single Resume Analysis", "Resume Shortlist"])

if selection == "Home":
    home.Main()
elif selection == "Single Resume Analysis":
    single_score.Main()
elif selection == "Resume Shortlist":
    shortlist.Main()