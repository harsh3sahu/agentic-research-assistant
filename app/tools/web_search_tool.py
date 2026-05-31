from app.config import Config
from tavily import TavilyClient

class WebSearchTool:
    def __init__(self):

        api_key=Config.TAVILY_API_KEY

        if not api_key:
            raise ValueError("Tavily api key not found")

        self.client=TavilyClient(api_key=api_key)

    def run(self,query:str,max_results:int=5):

        results= self.client.search(
            query=query,
            max_results=max_results,
            search_depth="advanced"
        )

        context = "\n\n".join(
            [
                result["content"]
                for result in results["results"]
            ]
        )

        sources=[
            {
                "title":result.get("title","unknown"),
                "url":result.get("url","")
            }
            for result in results["results"]
        ]

        return{
            "context":context,
            "sources":sources
        }
