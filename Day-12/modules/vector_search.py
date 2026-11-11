import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class VectorSearch:

    def __init__(self):
        self.documents = []

    def add_document(self, text, embedding, category, filename):
        self.documents.append({
            "text": text,
            "embedding": embedding,
            "category": category,
            "filename": filename
        })

    def search(self, query_embedding, top_k=5):

        if not self.documents:
            return []

        document_embeddings = np.array([
            doc["embedding"] for doc in self.documents
        ])

        similarities = cosine_similarity(
            [query_embedding],
            document_embeddings
        )[0]

        ranked_results = []

        for index, score in enumerate(similarities):
            result = {
                "text": self.documents[index]["text"],
                "category": self.documents[index]["category"],
                "filename": self.documents[index]["filename"],
                "similarity_score": float(score)
            }

            ranked_results.append(result)

        ranked_results.sort(
            key=lambda x: x["similarity_score"],
            reverse=True
        )

        return ranked_results[:top_k]