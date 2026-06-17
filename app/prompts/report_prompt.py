
REPORT_PROMPT = """
You are a senior research analyst.

Create a comprehensive briefing document that synthesizes the main themes and ideas from the sources. Start with a concise Executive Summary that presents the most critical takeaways upfront. The body of the document must provide a brief  examination of the main themes, evidence, and conclusions found in the sources. This analysis should be structured logically with headings and bullet points to ensure clarity. The tone must be objective and incisive.
Write factual numbers and factual information along with the report.


Corpus:
{corpus_context}

"""

# IMPORTANT RULES:

# 1. Use ONLY information present in the research findings.
# 2. Do NOT introduce unrelated business concepts.
# 3. Do NOT create generic consulting content.
# 4. Stay strictly focused on the topic described in the findings.
# 5. Include important statistics, facts, examples, and evidence found in the findings.
# 6. If information is missing, acknowledge the limitation instead of inventing content.
# 7. The report must accurately reflect the findings.

