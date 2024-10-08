from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore

load_dotenv()
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings


llm=ChatGoogleGenerativeAI(model="gemini-pro",google_api_key="<your-api-key>")
embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key="<your-api-key>")

path=r"C:\Users\ISH KUMAR JHA\Desktop\langchain_gen_ai\langchain-document\langchain.readthedocs.io\en\v0.1"

def ingest_docs():
    loader = ReadTheDocsLoader(r"langchain.readthedocs.io\en\v0.1",encoding="utf-8")

    raw_documents = loader.load()
    print(f"loaded {len(raw_documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)
    for doc in documents:
        new_url = doc.metadata["source"]
        new_url = new_url.replace("langchain.readthedocs.io", "https:/")
        doc.metadata.update({"source": new_url})

    print(f"Going to add {len(documents)} to Pinecone")
    PineconeVectorStore.from_documents(
        documents, embeddings, index_name="langchain-doc-index"
    )
    print("****Loading to vectorstore done ***")


if __name__ == "__main__":
    ingest_docs()