# Import Required Library 
from sentence_transformers import SentenceTransformer

# Load Pre-trained AI Embedding Model
model= SentenceTransformer('all-MiniLm-L6-v2')

# Create 50 Sentence Dataset
sentences = [
    #Programming
    "Python is a popular programming language.",
    "Java is used for software development.",
    "Programming helps solve real world problems.",
    "Python is easy to learn for beginners.",
    "Web development uses HTML CSS and JavaScript.",
    "Software engineers develop computer applications.",
    "Learning Python improves coding skills.",
    "Java programming is used in enterprise applications.",
    "Developers write code to build software.",
    "Programming is an important technical skill.",

    #AI
    "Artificial intelligence makes machines intelligent.",
    "Machine learning is a branch of artificial intelligence.",
    "AI helps computers make decisions.",
    "Deep learning uses neural networks.",
    "Artificial intelligence is changing the world.",
    "Chatbots use artificial intelligence.",
    "AI can recognize images and speech.",
    "Machine learning learns patterns from data.",
    "Robots can use AI to perform tasks.",
    "AI technology is growing rapidly.",

    #Education
    "Students learn new subjects at school.",
    "Education helps people gain knowledge.",
    "Online learning provides flexible education.",
    "Teachers help students understand lessons.",
    "Reading books improves knowledge.",
    "Universities provide higher education.",
    "Students prepare for examinations.",
    "Learning new skills improves career opportunities.",
    "Education is important for everyone.",
    "Online courses help people learn from home.",

    #Business
    "Businesses provide products and services.",
    "Marketing helps companies attract customers.",
    "Entrepreneurs start their own businesses.",
    "Financial management is important for companies.",
    "Customer service improves business relationships.",
    "Companies develop strategies to increase profits.",
    "Digital marketing promotes products online.",
    "Business management requires good leadership.",
    "Sales help businesses generate revenue.",
    "Technology improves business operations.",

    #Travel
    "Travel allows people to explore new places.",
    "Tourists visit different countries.",
    "Airplanes make international travel easier.",
    "Hotels provide accommodation for travelers.",
    "People enjoy visiting beautiful beaches.",
    "Travel helps people experience different cultures.",
    "Tourism supports the economy.",
    "Travelers explore historical places.",
    "Planning is important before travelling.",
    "People travel to discover new destinations."
]

# Import Numerical and Similarity Libraries
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Generate Sentence Embeddings
sentence_embeddings = model.encode(sentences)
print("Embedding Generation Completed!")
print("Embedding Shape:", sentence_embeddings.shape)

# Accept User Query
query = input("\nEnter your sentence:")
print("Your Query:", query)

# Generate Query Embedding
query_embedding = model.encode([query])
print("Query Embedding Shape:", query_embedding.shape)

# Calculate Cosine Similarity
similarity_scores = cosine_similarity(
    query_embedding,
    sentence_embeddings
)
print("Similarity Scores:")
print(similarity_scores)

# Rank Sentences by Similarity
ranked_indices = np.argsort(similarity_scores[0])[::-1]
print("\nRanked Sentences:")

# Display Topn  5 Similar Sentences 
print("\nTop 5 Similar Sentences:")
for index in ranked_indices[:5]:
    print("\nSentence:", sentences[index])
    print("Similarity score:", similarity_scores[0][index])

    