from pypdf import PdfReader

class DocumentLoader:

    def load_pdf(self,file_path:str):
        reader=PdfReader(file_path)
        documents=[]

        for page_number, page in enumerate(reader.pages):
            text=page.extract_text()
            if not text:
                continue




            documents.append(
                {
                    "content":text,
                    "metadata":{
                        "source_file":file_path,
                        "page":page_number+1
                    }
                }
            )

        return documents


        

document_loader = DocumentLoader()