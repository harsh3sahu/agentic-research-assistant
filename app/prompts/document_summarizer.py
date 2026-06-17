DOCUMENT_SUMMARIZE_PROMPT = """
You are an expert document analyst.
Summarize the following document section.
Preserve:
- Main themes
- Important findings
- Key facts
- Statistics
- Recommendations
- Conclusions
Keep the summary short with factual information.

Document:

{context}
"""