from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import json

# Adjusting sys.path to import from parent directory
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.config import OPENAI_API_KEY
from app.config import LLM_MODEL

# Initialize the LLM
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=LLM_MODEL, temperature=0)

# Define the prompt template
prompt = PromptTemplate(
    input_variables=["resume_text", "jd_text"],
    template="""
You are an experienced technical recruiter. Evaluate the candidate against the job description.

Return ONLY JSON in this format:

{{
  "score": 0-100,
  "analysis": "concise analysis"
}}

--- Job Description ---
{jd_text}

--- Resume ---
{resume_text}
"""
)


# Function to evaluate model response
def evaluate_model_response(resume_text: str, jd_text: str) -> dict:
    """
    Returns Structured output:
    {
        "score: int (0-100),
        "analysis}: "detailed feedback"
    }
    """

    chain = prompt | llm
    response = chain.invoke({"resume_text": resume_text, "jd_text": jd_text})

    try:
        return json.loads(response.content)  # response is an AIMessage
    except:
        return {"score": 0, "analysis": "Invalid model output"}