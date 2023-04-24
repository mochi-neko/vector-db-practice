import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=".chromadb/"
))

client.heartbeat()
client.reset()

from chromadb.utils import embedding_functions

collection = client.get_or_create_collection(
    name="collection_with_date",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"))

import datetime

collection.add(
    documents=[
        "An apple is a red rounded fruit.",
        "An orange is an orange rounded fruit.",
        "A fruit is rounded.",
    ],
    metadatas=[
        {
            "datetime": datetime.datetime(year=2023, month=4, day=1).strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(year=2023, month=4, day=2).strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(year=2023, month=4, day=15).strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
    ],
    ids=[
        "0",
        "1",
        "2",
    ]
)

print(collection.query(
    query_texts=["What is an apple?"],
    n_results=1
))
# -> "An apple is a red rounded fruit."

print(collection.query(
    query_texts=["Orange"],
    n_results=1
))
# -> "An orange is an orange rounded fruit."

result = collection.get(
    ids=["2"],
    include=["documents", "embeddings", "metadatas"]
)

print(result.get("documents")[0])
# -> "A fruit is rounded."

print(len(result.get("embeddings")[0]))
# -> 384 (= dimension of the embedding vector

print(result.get("metadatas")[0]["datetime"])
# -> "2023-04-15 00:00:00.000000"