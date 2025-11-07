from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_top_n_resumes(job_embedding, resume_embeddings, n):
    """
    Get the top N resumes based on cosine similarity to the job description embedding.
    
    Parameters:
    job_embedding (np.array): Embedding vector for the job description.
    resume_embeddings (list of np.array): List of embedding vectors for resumes.
    n (int): Number of top resumes to return.
    """
    
    similarity_scores = []

    for file_name, embedding in resume_embeddings.items():
        similarity = cosine_similarity(
            np.array(job_embedding).reshape(1, -1),
            np.array(embedding).reshape(1, -1)
        )[0][0]
        similarity_scores.append((file_name, similarity))
    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    return similarity_scores[:n]