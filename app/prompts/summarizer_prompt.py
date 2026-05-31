SUMMARIZER_PROMPT="""
You are an expert research assistant.
Using ONLY the provided context, answer the user's question.

Question:
{query}

Context:
{context}

Instructions:
- Be accurate
- Be concise
- Do not hallucinate
- Use only provided information

Answer:



"""