class ResearchAgent:

    def __init__(
        self,
        tool
    ):

        self.tool = tool

    def run(
        self,
        query: str
    ):

        print(
            f"\nResearch Agent received query: {query}"
        )

        return self.tool.run(query=query)