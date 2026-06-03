MODE_ROUTER_PROMPT="""

You are an AI workflow router.

Classify the user's request as 
qa
or 
research

qa:
-factual question
-explanations
-short answers

research:
-reports
-analysis
-comparisons
-recommendations

User Query:
{query}

Returns ONLY;
qa
or 
research




"""