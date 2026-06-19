# from app.graph.workflow import graph

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

# results = (
#             vector_store.collection.get(
#                 include=["documents"]
#             )
#         )

# print(len(results))
# print(results)

from app.agents.report_agent import report_agent

# response=report_agent.generate_report()

# print(len(response.get("report","No report generated")))

# with open(
#             "report.txt",
#             "w",
#             encoding="utf-8"
#         ) as f:
#             f.write(response.get("report","No report generated"))

# print("report saved")


from app.vectorstore.chroma_manager import chroma_manager

print(chroma_manager.collection.metadata)
# print(type(chroma_manager.collection))
# print(dir(chroma_manager.collection))