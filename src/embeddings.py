from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embedding(text: str):
    """
    Create embedding for the given text using a pre-trained model.
    """
    embedding = embed_model.encode(text)
    return embedding

def resume_batch_create_embeddings(resume_dict: dict):
    """
    Create embeddings for a batch of texts.
    """
    embeddings = {}
    for filename, text in resume_dict.items():
        embeddings[filename] = embed_model.encode(text)
    return embeddings
