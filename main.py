# from app.rag.hybrid_retriever import hybrid_retriever

# results = hybrid_retriever.retrieve(
#     "impact of msme for women in gujarat"
# )

# semantic_results = results["semantic"]
# bm25_results = results["bm25"]

# print("\nSemantic")
# for doc in semantic_results:
#     print(doc["id"])

# print("\nBM25")
# for doc in results["bm25"]:
#     print(doc["id"])

# print("\nSEMANTIC")

# for doc in semantic_results:

#     print(len(doc["content"]))
#     print(doc["distance"])



# for doc in semantic_results[:3]:

#     print("=" * 50)

#     print(doc["content"])


# print("\nBM25")

# for doc in bm25_results[:3]:

#     print("=" * 50)

#     print(doc["content"])


from app.vectorstore.vector_store import vector_store

results = vector_store.collection.get(
    include=["documents"]
)

# documents = results["documents"]

# lengths = []

# for i, doc in enumerate(documents):

#     lengths.append({
#         "chunk_id": i + 1,
#         "chars": len(doc),
#         "words": len(doc.split())
#     })

# lengths = sorted(
#     lengths,
#     key=lambda x: x["words"]
# )

# for item in lengths[:20]:

#     print(item)


#     results = vector_store.collection.get(
#     include=["documents"]
# )

# documents = results["documents"]

# for doc in documents:

#     if len(doc.split()) < 15:

#         print("=" * 80)

#         print(doc)





# from app.rag.document_loader import document_loader

# documents = document_loader.load_pdf(
#     "data/Gujarat-Report-1.pdf"
# )

# print(len(documents))

# for doc in documents:
#     print(len(doc["content"]))
from app.vectorstore.vector_store import vector_store

vector_store.count()



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

