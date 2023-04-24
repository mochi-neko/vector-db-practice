# https://docs.trychroma.com/usage-guide

# Initiating the Chroma client
import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=".chromadb/"  # Optional, defaults to .chromadb/ in the current directory
))

client.heartbeat()  # returns a nanosecond heartbeat. Useful for making sure the client remains connected.
client.reset()  # Empties and completely resets the database. ⚠️ This is destructive and not reversible.

# Using collections

from chromadb.utils import embedding_functions

# Creating, inspecting, and deleting Collections

# Get a collection object from an existing collection, by name. If it doesn't exist, create it.
collection = client.get_or_create_collection(
    name="my_collection",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"))  # Default embedding function

collection.peek()  # returns a list of the first 10 items in the collection
collection.count()  # returns the number of items in the collection

# Adding data to a Collection

collection.add(
    documents=[
        "lorem ipsum...",
        "doc2",
        "doc3",
    ],
    metadatas=[
        {"chapter": "3", "verse": "16"},
        {"chapter": "3", "verse": "5"},
        {"chapter": "29", "verse": "11"},
    ],
    ids=[
        "id1",
        "id2",
        "id3",
    ]
)

# Querying a Collection

print(collection.query(
    query_texts=["doc10", "thus spake zarathustra", ...],
    n_results=10,
    where={"metadata_field": "is_equal_to_this"},
    where_document={"$contains":"search_string"}
))

print(collection.get(
    ids=["id1", "id2", "id3", ...],
    where={"style": "style1"}
))


# Only get documents and ids
print(collection.get(
    include=["documents"]
))

print(collection.query(
    query_embeddings=[[11.1, 12.1, 13.1],[1.1, 2.3, 3.2]],
    include=["documents"]
))

# Updating data in a collection

collection.update(
    ids=["id1", "id2", "id3", ...],
    embeddings=[[1.1, 2.3, 3.2], [4.5, 6.9, 4.4], [1.1, 2.3, 3.2], ...],
    metadatas=[{"chapter": "3", "verse": "16"}, {"chapter": "3", "verse": "5"}, {"chapter": "29", "verse": "11"}, ...],
    documents=["doc1", "doc2", "doc3", ...],
)
