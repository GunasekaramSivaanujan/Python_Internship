# Import Libraries
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load AI Model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Knowledge Base - 15 Documents
documents = [
    # Python Documents
    "Python is a popular programming language.",
    "Python is used for web development.",
    "Python supports object oriented programming.",
    "Python is useful for automation.",
    "Python has many built in libraries.",

    # NumPy Documents
    "NumPy is a Python library for numerical computing.",
    "NumPy provides powerful array operations.",
    "NumPy is useful for mathematical calculations.",
    "NumPy supports multidimensional arrays.",
    "NumPy is widely used in data science.",

    # Pandas Documents
    "Pandas is a Python library for data analysis.",
    "Pandas provides DataFrame and Series.",
    "Pandas helps to clean and organize data.",
    "Pandas can read CSV and Excel files.",
    "Pandas is widely used in data science."

    # Machine Learning Documents
    "Machine learning allows computers to learn from data.",
    "Machine learning is a branch of artificial intelligence.",
    "Machine learning models identify patterns in data.",
    "Supervised learning uses labeled training data.",
    "Machine learning is used for prediction."

    # Deep Learning Documents
    "Deep learning uses artificial neural networks.",
    "Deep learning is a part of machine learning.",
    "Neural networks are inspired by the human brain.",
    "Deep learning is used in image recognition.",
    "Deep learning helps computers understand speech."

     # AI Documents
    "Artificial intelligence enables machines to perform intelligent tasks.",
    "AI is used in healthcare and education.",
    "AI systems can understand human language.",
    "Chatbots use artificial intelligence to answer questions.",
    "AI helps computers solve complex problems."

     # Additional Python Documents
    "Python supports functions and modules.",
    "Python is beginner friendly.",
    "Python is used in artificial intelligence.",

    # Additional NumPy Documents
    "NumPy arrays are faster than Python lists.",
    "NumPy supports matrix operations.",
    "NumPy is useful for scientific computing.",

    # Additional Pandas Documents
    "Pandas supports data filtering.",
    "Pandas can handle missing values.",
    "Pandas is useful for data visualization.",

    # Additional Machine Learning Documents
    "Machine learning uses algorithms to learn patterns.",
    "Classification is a machine learning technique.",
    "Regression is used to predict numerical values.",

    # Additional Deep Learning Documents
    "Deep learning uses multiple neural network layers.",
    "CNNs are used for image processing.",
    "Deep learning requires large amounts of data.",
   
    # Additional AI Documents
    "Artificial intelligence is changing technology.",
    "AI can automate repetitive tasks.",
    "Natural language processing is a field of AI.",
    "AI is used in recommendation systems.",
    "Generative AI can create text and images."
]

embeddings = model.encode(documents)
np.save("document_embeddings.npy", embeddings)
print("Embedding Shape:", embeddings.shape)

#Get user query
query = input("Enter your search query: ")
query_embedding = model.encode([query])
similarity_scores = cosine_similarity(query_embedding, embeddings)[0]
ranked_indices = np.argsort(similarity_scores)[::-1]

print("\nTop 5 Search Results:")
for index in ranked_indices[:5]:
    print("\nDocument:", documents[index])
    print("Similarity Score:", similarity_scores[index])