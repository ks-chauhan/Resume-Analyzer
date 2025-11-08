# ResumeAnalyzer – AI Resume Scoring and Shortlisting System

This is a Streamlit-based application that evaluates resumes against a given Job Description (JD). It supports both:
1. Single resume scoring
2. Shortlisting and ranking multiple resumes

The application combines embeddings-based similarity and LLM-based evaluation to produce a score and written analysis.

---

## Features

1. Single Resume Analysis  
   - Upload one resume and provide a job description
   - The system evaluates the resume using an LLM and returns:
     - A score (0–100)
     - Analysis explaining strengths and weaknesses

2. Resume Shortlisting (Top-N Ranking)
   - Upload multiple resumes
   - The system:
     - Converts each resume and JD to embeddings
     - Uses cosine similarity to shortlist resumes
     - Applies LLM evaluation to shortlist candidates and generate a score and analysis


---


## Setup the Project on Your System

1. Clone the repository : 

git clone https://github.com/ks-chauhan/Resume-Analyzer/tree/main
\n
cd Resume-Analyzer

2. Create and activate a Python virtual environment

python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Mac/Linux)

3. Install required dependencies

pip install -r requirements.txt

4. Create a `.env` file in the project root and add your OpenAI key  

OPENAI_API_KEY = "your_openai_api_key"

5. Run the application

streamlit run app/main.py

---

The site is deployed here : https://dayworks-resume-analyzer.streamlit.app/
