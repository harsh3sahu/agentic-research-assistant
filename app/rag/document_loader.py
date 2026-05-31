from pypdf import PdfReader

class DocumentLoader:

    def load_pdf(self,file_path:str):
        reader=PdfReader(file_path)

        documents=[]

        for page_number, page in enumerate(reader.pages,start=1):
            text=page.extract_text()

            if not text:
                continue


            documents.append(
                {
                    "content":text,
                    "metadata":{
                        "source_file":file_path,
                        "page":page_number
                    }
                }
            )

        return documents

document_loader = DocumentLoader()