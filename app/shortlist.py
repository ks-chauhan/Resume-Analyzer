import streamlit as st

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.resume_parser import pdf_parser
from src.processor import process_multiple_resumes

def Main():
    """
    Resume Shortlist Page
    """
    st.title("Shortlist Resumes")
    st.markdown("This is where you can shortlist resumes based on job descriptions.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Job Description")
        job_description = st.text_area("Enter Job Description",
                                       height=300,
                                       placeholder="Paste the job description here...")
    with col2:
        st.subheader("Resume Upload")
        resume_files = st.file_uploader("Upload Resume Files",
                                        accept_multiple_files = True,
                                        type=["pdf"],
                                        help="Upload pdf files containing candidates' resumes.")
        if resume_files:
            st.success(f"{len(resume_files)} resumes uploaded successfully!")
        
        N = st.number_input("Number of Resumes to Shortlist")
    
    button = st.button("Shortlist Resumes")
    if button:
        if not job_description.strip():
            st.error("A job description is required for analysis.")
            return
        if not resume_files:
            st.error("Please upload atleast one resume file for analysis.")
            return
        if N <= 0:
            st.error("Please enter a valid number of resumes to shortlist.")
            return
        
        with st.spinner("Shortlisting resumes..."):
            resumes_dict = {}

            for resume_file in resume_files:
                resume_text = pdf_parser(resume_file)
                resumes_dict[resume_file.name[0:-4]] = resume_text
            results = process_multiple_resumes(resumes_dict, job_description.strip(), int(N))
            
            for item in results:
                st.subheader(f"Resume: {item['file_name']}")

                st.metric(
                    label="Final Score",
                    value=f"{item['score']}/100",
                    delta=f"Similarity: {item['similarity']:.4f}"
                )

                with st.expander("View Analysis"):
                    st.write(item['analysis'])
                
                st.markdown("---")


            
