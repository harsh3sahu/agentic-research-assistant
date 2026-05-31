CRITIC_PROMPT="""
You are a quality assurance agent.

Evaluate the answer.

Question:
{query}

Answer:
{answer}

Context:
{context}

Return:

CONFIDENCE :<0.0-1.0>

FEEDBACK:
<feedback>

Does the answer accurately reflect the contexts?



"""