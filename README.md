**LangChain - Documentation Ingestion Bot**
**Author: Ish Jha
Contact Info: ishjha1929@gmail.com / jha.13@alumni.iitj.ac.in
(Please feel free to contact for any doubts or collaborative projects!)**

This project is designed to ingest and index web-scraped documentation from the entire LangChain documentation site into Pinecone for vector-based search.
It leverages LangChain, Google Generative AI, and Pinecone to split and store documentation in a format suitable for efficient search and retrieval.

**Requirements**
Python 3.8+
LangChain
Pinecone
langchain_google_genai
langchain_community
dotenv

**Installation**
Clone the repository:
git clone https://github.com/yourusername/documentation-ingestion-bot.git
cd documentation-ingestion-bot

**Install the required packages using Pipenv:**
pipenv install
Activate the Pipenv shell:
pipenv shell

Set up your environment variables:
Create a .env file in the root directory.
Add your Google API key:
GOOGLE_API_KEY=your-google-api-key
Add your Pinecone api key
PINECONE_API_KEY=your-pinecone-api-key

**Usage**
To ingest and index the web-scraped LangChain documentation:
Ensure the path to the documentation is correctly set in the code:
path = r"C:\path\to\your\documentation"

**Run the ingestion script:**
python ingest_docs.py

**How It Works**
Documentation Loading: The ReadTheDocsLoader is used to load documentation from the specified path.

Text Splitting: The RecursiveCharacterTextSplitter splits the documents into manageable chunks for indexing.

Vectorization: Each chunk is vectorized using Google Generative AI embeddings.

Pinecone Indexing: The vectorized documents are stored in Pinecone, allowing for fast and efficient search.

**Author: Ish Jha
Contact Info: ishjha1929@gmail.com / jha.13@alumni.iitj.ac.in
(Please feel free to contact for any doubts or collaborative projects!)**

