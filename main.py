from app.graph.workflow import graph

from app.vectorstore.vector_store import vector_store

# vector_store.count()
# vector_store.clear()
print(vector_store.count())

# from IPython.display import Image, display
# png_data = graph.get_graph().draw_mermaid_png()

# with open("langgraph1updated.png", "wb") as f:
#     f.write(png_data)

# response=graph.invoke({"query":"what is ipl and its winners list"})

# print("*"*50)
# print(response["answer"])
# print(response["context"])

results = (
            vector_store.collection.get(
                include=["documents"]
            )
        )

print(len(results))
# print(results)