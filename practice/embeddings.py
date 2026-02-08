from typing import List
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core import Document

class VectorStore:
    """
    Manage vector sore for the application
    """
    def __init__(self):
        self.embedding=HuggingFaceEmbeddings()
        self.vectorstore=None
        self.retriever=None

    
    def create_retriever(self, documents=List[Document]):
        self.vectorstore=FAISS.from_documents(documents, self.embedding)
        self.retriever=self.vectorstore.as_retriever()


    def retrieve(self, query):
        self.retriever.invoke({"input": query}, config={"k": k})

    def generate_answer(self):
        context = "\n\n".join([doc.page_content for doc in state.retrieved_docs])

        prompt = f""" Answer the questions based on the context

        Context:
        {context}

        Question: {state.question}   """

        response = self.llm.invoke(prompt)
        answer = response.content if hasattr(response, 'content') else str(response)
