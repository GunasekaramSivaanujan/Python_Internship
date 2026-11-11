from document_loader import DocumentLoader
from modules.embedding import EmbeddingGenerator
from modules.vector_search import VectorSearch
from modules.document_processor import DocumentProcessor

loader = DocumentLoader()
processor = DocumentProcessor()
embedding_generator = EmbeddingGenerator()
vector_search = VectorSearch()

documents = loader.load_documents("dataset")

for document in documents:
    chunks = processor.process_document(document["text"])

    for chunk in chunks:
        embedding = embedding_generator.generate_embedding(chunk)

        vector_search.add_document(
            chunk,
            embedding,
            document["category"],
            document["filename"]
        )

test_queries = [
    ("What is Python?", "Python"),
    ("What are Python lists?", "Python"),
    ("What is a Python dictionary?", "Python"),
    ("What are Python functions?", "Python"),
    ("What is NumPy?", "NumPy"),
    ("What are NumPy arrays?", "NumPy"),
    ("What is matrix multiplication?", "NumPy"),
    ("What is Pandas?", "Pandas"),
    ("What is a DataFrame?", "Pandas"),
    ("How does Pandas handle missing values?", "Pandas"),
    ("What is Machine Learning?", "Machine_Learning"),
    ("What is supervised learning?", "Machine_Learning"),
    ("What is classification?", "Machine_Learning"),
    ("What is regression?", "Machine_Learning"),
    ("What is Deep Learning?", "Deep_Learning"),
    ("What are neural networks?", "Deep_Learning"),
    ("What is image recognition?", "Deep_Learning"),
    ("How should employees protect passwords?", "Company_Policies"),
    ("What is company data confidentiality?", "Company_Policies"),
    ("What is technical training?", "Training_Information")
]

top1_correct = 0
top5_correct = 0

for query, expected_category in test_queries:
    query_embedding = embedding_generator.generate_embedding(query)

    results = vector_search.search(
        query_embedding,
        top_k=5
    )

    if results:
        if results[0]["category"] == expected_category:
            top1_correct += 1

        if any(
            result["category"] == expected_category
            for result in results
        ):
            top5_correct += 1

total = len(test_queries)

print("\n===== RETRIEVAL EVALUATION =====")
print("Total Test Queries:", total)
print("Top-1 Correct:", top1_correct)
print("Top-5 Correct:", top5_correct)

print("Top-1 Accuracy:", round(top1_correct / total * 100, 2), "%")
print("Top-5 Accuracy:", round(top5_correct / total * 100, 2), "%")