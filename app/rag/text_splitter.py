from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import Config



class TextSplitter:

    def __init__(self):

        self.splitter=RecursiveCharacterTextSplitter(chunk_size=Config.CHUNK_SIZE,chunk_overlap=Config.CHUNK_OVERLAP)


    

    def split_documents(self,documents:list):

        chunks=[]

        for document in documents:

            content=document["content"]

            metadata=document["metadata"]

            split_texts= self.splitter.split_text(content)



            for chunk_id, chunk in enumerate (split_texts):

                chunks.append({
                    "content":chunk,
                    "metadata":{
                        **metadata,
                        "chunk_id":chunk_id
                    }
                })



        return chunks


text_splitter=TextSplitter()
    