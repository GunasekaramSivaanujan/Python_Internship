# Import Required Libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Create 10 Documents
documents = [
    "Python is popular programming language.",
    "Python is used for web development.",
    "Artificial Intelligence makes machines smart.",
    "AI helps computers slove problems.",
    "Machine Learning is a part of AI.",
    "Machine Learning uses data to make predictions.",
    "Football is a popular sport.",
    "Cricket is played in many countries.",
    "Travel helps people explore new places.",
    "Tourism is important for many countries."
]

# Display All Documents
for index, document in enumerate(documents):
    print("Document", index + 1,":", document)

# Convert Documents into vectors
vectroizer = TfidfVectorizer()
document_vectors = vectroizer.fit_transform(documents)
print("Documents Vectors:")
print(document_vectors.toarray())

# Accept User Query 
query = input("\nEnter your question:")
print("Your Query:", query)

# Convert User Query into Vector
query_vector = vectroizer.transform([query])
print("Query Vector:")
print(query_vector.toarray())

#Calculate Cosine Similarity
similarity_scores = cosine_similarity(
    query_vector,
    document_vectors
)
print("Similarity Scoures:")
print(similarity_scores)

# Rank Documents Based on Similarity
ranked_indices = np.argsort(similarity_scores[0])[::-1]
print("\nRanked Documents:")
for index in ranked_indices:
    print(
        "Document", index +1,
        "Similarity:", similarity_scores[0][index]
    )

# Display Top Documents
print("\nTop 3 Simiar Documents:")
for index in ranked_indices[:3]:
    print("\nDocument:", documents[index])
    print("Similarity Score:", similarity_scores[0][index])

# Create Similarity Matrix
similarity_matrix = cosine_similarity(document_vectors)
print("\nDocuments Similarity Matrix:")
print(similarity_matrix)