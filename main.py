from app.rag.ingestion_pipeline import ingestion_pipeline

ingestion_pipeline.ingest_folder('data')

from app.vectorstore.vector_store import vector_store

results = vector_store.collection.get(
    include=["documents"]
)

documents = results["documents"]

print(f"Total Chunks: {len(documents)}")

print("\nChunk Length Statistics")
print("=" * 50)

word_counts = [
    len(doc.split())
    for doc in documents
]

print(f"Min Words: {min(word_counts)}")
print(f"Max Words: {max(word_counts)}")
print(f"Average Words: {sum(word_counts)/len(word_counts):.2f}")

print("\nAll Chunk Lengths")
print("=" * 50)

for i, doc in enumerate(documents):

    print(
        f"Chunk {i+1}: "
        f"{len(doc.split())} words | "
        f"{len(doc)} chars"
    )