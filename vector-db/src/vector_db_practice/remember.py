import datetime

import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=".chromadb/"
))

client.heartbeat()
client.reset()

from chromadb.utils import embedding_functions

buffer = client.get_or_create_collection(
    name="buffer",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"))

import datetime

buffer.add(
    documents=[
        "Tom: Hello, Ken.",
        "Ken: Hello, Tom. How are you?",
        "Tom: I'm fine, thanks. And you?",
        "Ken: I'm fine, too. Where are you going?",
        "Tom: I'm going to the library.",
        "Ken: I'm going to the library, too. Let's go together.",
        "Tom: OK. Let's go.",
        "Ken: What are you going to do at the library?",
        "Tom: I'm going to read a book.",
        "Ken: What book are you going to read?",
        "Tom: I'm going to read a book about history.",
        "Ken: I'm going to read a book about science.",
        "Tom: That sounds interesting.",
        "Ken: Yes, it does.",
        "Tom: What are you going to do after the library?",
        "Ken: I'm going to the gym.",
        "Tom: I'm going to the gym, too. Let's go together.",
        "Ken: OK. Let's go.",
        "Tom: What are you going to do at the gym?",
        "Ken: I'm going to lift weights.",
    ],
    metadatas=[
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=0, second=0)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=0, second=5)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=0, second=10)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=0, second=15)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=0, second=20)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=0, second=25)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=0, second=30)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=0, second=35)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=0, second=40)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=0, second=45)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=0, second=50)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=0, second=55)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=1, second=0)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=1, second=5)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=1, second=10)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=1, second=15)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=1, second=20)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=1, second=25)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=1, second=30)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
        {
            "datetime": datetime.datetime(
                year=2023, month=4, day=1,
                hour=12, minute=1, second=35)
            .strftime("%Y/%m/%d %H:%M:%S.%f"),
        },
    ],
    ids=[
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
    ]
)

print(buffer.query(
    query_texts=["What kind of book Tom read at the library?"],
    n_results=4
))


