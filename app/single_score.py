import streamlit as st

# Parent Directory Import
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.resume_parser import pdf_parser
from src.processor import process_single_resume

def Main():
    """
    Single Resume Analysis Page
    """

    st.title("Single Resume Analysis")
    st.markdown("This is where you can analyze a single resume in detail.")
    
    col1, col2 = st.columns(2)

    with col1:
        # Job Description Input
        st.subheader("Job Description")
        job_description = st.text_area("Enter Job Description",
                                       height = 300,
                                       placeholder = "Paste the job description here...")
    with col2:
        # Resume Upload
        st.subheader("Resume Upload")
        resume_file = st.file_uploader("Upload Resume File",
                                       accept_multiple_files = False,
                                       type = ["pdf"],
                                       help = "Upload a pdf file containing cadidate's resume.")
        if resume_file:
            st.success("Resume uploaded successfully!")
        
    analyze_button = st.button("Perform Analysis")
    
    if analyze_button:
        # Input Validations
        if not job_description.strip():
            st.error("A job description is required for analysis.")
            return
        if not resume_file:
            st.error("Please upload a resume file for analysis.")
            return
        
        # Analysis Process
        with st.spinner("Analyzing the resume..."):
            resume_text = pdf_parser(resume_file)
            result = process_single_resume(resume_text, job_description.strip())
            
            st.subheader("Analysis Result")

            st.metric(
                label = "Final Score",
                value = f"{result['score']}/100")
            
            st.markdown("### Detailed Analysis")
            st.write(result['analysis'])

