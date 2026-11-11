import streamlit as st

from document_loader import DocumentLoader
from modules.embedding import EmbeddingGenerator
from modules.vector_search import VectorSearch
from modules.document_processor import DocumentProcessor


st.set_page_config(
    page_title="AI Knowledge Base Search System",
    layout="wide"
)

st.title("AI Knowledge Base Search System")

st.write(
    "Search information from company and educational documents "
    "using semantic meaning."
)


# Initialize modules
loader = DocumentLoader()
processor = DocumentProcessor()


@st.cache_resource
def get_embedding_model():
    return EmbeddingGenerator()


embedding_model = get_embedding_model()


# Initialize vector search
if "vector_search" not in st.session_state:
    st.session_state.vector_search = VectorSearch()
    st.session_state.processed = False


# Load dataset documents
if not st.session_state.processed:

    documents = loader.load_documents("dataset")

    for document in documents:

        chunks = processor.process_document(document["text"])

        for chunk in chunks:

            embedding = embedding_model.generate_embedding(chunk)

            st.session_state.vector_search.add_document(
                chunk,
                embedding,
                document["category"],
                document["filename"]
            )

    st.session_state.processed = True

    st.success(
        str(len(documents)) + " documents loaded successfully!"
    )


# Document Upload
st.subheader("1. Document Upload")

uploaded_files = st.file_uploader(
    "Upload text documents",
    type=["txt"],
    accept_multiple_files=True
)


if st.button("Process Documents"):

    if uploaded_files:

        for file in uploaded_files:

            text = file.getvalue().decode("utf-8")

            chunks = processor.process_document(text)

            for chunk in chunks:

                embedding = embedding_model.generate_embedding(chunk)

                st.session_state.vector_search.add_document(
                    chunk,
                    embedding,
                    "Uploaded",
                    file.name
                )

        st.success("Documents processed successfully!")

    else:
        st.warning("Please upload documents first.")


st.divider()


# Semantic Search
st.subheader("2. Semantic Search")

query = st.text_input(
    "Enter your question",
    placeholder="Example: What happens if I miss my training session?"
)


if st.button("Search"):

    if query.strip():

        # Generate query embedding
        query_embedding = embedding_model.generate_embedding(query)

        # Retrieve Top 5 results
        results = st.session_state.vector_search.search(
            query_embedding,
            top_k=5
        )

        if results:

            # AI Answer using retrieved information
            st.subheader("3. AI Answer")

            best_result = results[0]

            st.write(best_result["text"])

            st.caption(
                "Answer generated from the retrieved document: "
                + best_result["filename"]
            )

            st.divider()

            # Result Display
            st.subheader("4. Search Results")

            st.write("Query:", query)

            st.write("Top 5 Relevant Results")

            for i, result in enumerate(results, start=1):

                st.write("Result:", i)

                st.write(
                    "Source Document:",
                    result["filename"]
                )

                st.write(
                    "Category:",
                    result["category"]
                )

                st.write(
                    "Similarity Score:",
                    round(result["similarity_score"], 4)
                )

                st.write(
                    "Relevant Text:",
                    result["text"]
                )

                st.divider()

        else:

            st.warning("No matching documents found.")

    else:

        st.warning("Please enter a question.")