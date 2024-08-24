from dotenv import load_dotenv
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain

load_dotenv()
from typing import Any, Dict, List
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import RetrievalQA
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

llm=ChatGoogleGenerativeAI(model="gemini-pro",google_api_key="<your-api-key>")
embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key="<your-api-key>")
INDEX_NAME = "langchain-doc-index"
def run_llm(query: str,chat_history: List[Dict[str, Any]] = []):

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key="<your-api-key>")
    docsearch = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)
    chat = ChatGoogleGenerativeAI(model="gemini-1.5-flash-001",google_api_key="<your-api-key>")

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")
    stuff_documents_chain = create_stuff_documents_chain(chat, retrieval_qa_chat_prompt)
    history_aware_retriever = create_history_aware_retriever(
        llm=chat, retriever=docsearch.as_retriever(), prompt=rephrase_prompt
    )

    qa = create_retrieval_chain(
        retriever=history_aware_retriever, combine_docs_chain=stuff_documents_chain
    )
    result = qa.invoke(input={"input": query, "chat_history": chat_history})
    return result



if __name__ == "__main__":
    res = run_llm(query="What is a LangChain Chain?")
    print(res["answer"])
