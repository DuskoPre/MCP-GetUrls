from app.models import SelectionRequest, SelectionResponse, SearchResult
from sentence_transformers import SentenceTransformer, util
import numpy as np
import random

# Load pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

def select_best_results(request: SelectionRequest) -> SelectionResponse:
    # Extract titles and snippets from search results
    titles_snippets = [f"{result.title} {result.snippet}" for result in request.results]

    # Encode titles and snippets
    embeddings = model.encode(titles_snippets, convert_to_tensor=True)

    # Compute cosine similarities
    cos_scores = util.cos_sim(embeddings, embeddings)

    # Convert to numpy array for easier manipulation
    cos_scores_np = cos_scores.numpy()

    # Remove diagonal elements (self-similarity)
    np.fill_diagonal(cos_scores_np, 0)

    # Calculate average similarity for each result
    avg_similarities = np.mean(cos_scores_np, axis=1)

    # Sort indices by average similarity in descending order
    sorted_indices = np.argsort(avg_similarities)[::-1]

    # Select top N results
    selected_indices = sorted_indices[:request.num_results]
    selected_results = [request.results[i] for i in selected_indices]

    # Generate reasoning (simple placeholder for now)
    reasoning = f"Selected top {request.num_results} results based on average similarity scores."

    return SelectionResponse(selected_results=selected_results, reasoning=reasoning)
