import json

from tqdm import tqdm
from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.rag.embeddings import embeddings


DATA_PATH = "data/fatawa.json.json"
PERSIST_DIRECTORY = "chroma_db"
BATCH_SIZE = 50


def load_documents():

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        fatawa = json.load(f)

    docs = []

    for item in fatawa:

        question = item["conversations"][0]["content"]
        answer = item["conversations"][1]["content"]

        docs.append(
            Document(
                page_content=f"""Question:
{question}

Answer:
{answer}
""",
                metadata={
                    "question": question,
                    "category": item["category"],
                },
            )
        )

    return docs


def ingest():

    docs = load_documents()

    vector_store = None

    for i in tqdm(range(0, len(docs), BATCH_SIZE)):

        batch = docs[i:i + BATCH_SIZE]

        if vector_store is None:

            vector_store = Chroma.from_documents(
                documents=batch,
                embedding=embeddings,
                persist_directory=PERSIST_DIRECTORY,
            )

        else:

            vector_store.add_documents(batch)

    print("✅ Chroma DB created successfully.")


if __name__ == "__main__":
    ingest()