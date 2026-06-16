from app.graph.workflow import graph

# from IPython.display import Image, display
# png_data = graph.get_graph().draw_mermaid_png()

# with open("langgraph1updated.png", "wb") as f:
#     f.write(png_data)

response=graph.invoke({"query":"what is ipl and its winners list"})

print("*"*50)
print(response["answer"])
print(response["context"])