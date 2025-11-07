from src.embeddings import create_embedding, resume_batch_create_embeddings
from src.llm_evaluator import evaluate_model_response
from src.scorer import get_top_n_resumes

def process_single_resume(resume_text: str, jd_text: str):
    """
    Process a single resume against a job description.
    Returns the evaluation result from the LLM.
    """
    return evaluate_model_response(resume_text, jd_text)

def process_multiple_resumes(resume_dict: dict, jd_text: str, n: int):
    
    jd_embedding = create_embedding(jd_text)
    resume_embeddings = resume_batch_create_embeddings(resume_dict)

    shortlisted = get_top_n_resumes(jd_embedding, resume_embeddings, n)

    results = []
    for file_name, sim_score in shortlisted:
        resume_text = resume_dict[file_name]
        evaluation = evaluate_model_response(resume_text, jd_text)
        results.append({
            "file_name": file_name,
            "similarity": sim_score,
            "score": evaluation['score'],
            "analysis": evaluation['analysis']
        })
    return results