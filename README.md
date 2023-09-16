# LangChain Legal Assistant
This is a personal project to build a conversational AI assistant for legal research using LangChain and ChromaDB. 

The goal of this project is to create an example of an AI that can answer questions about legal documents by retrieving relevant passages from a large database of legal texts.
It uses the LangChain library, ChromaDB, and OpenAI's GPT-3.5 model to implement conversational retrieval over a database of legal documents.

# Key Features
1. Loads PDF documents from a local folder into a Chroma vector database using PyPDFLoader
2. Uses OpenAI embeddings to index the documents
3. Implements conversational retrieval using GPT-3.5, LangChain, and a Chroma database
4. Runs on Google Colab for easy prototyping and leverages Google Drive for storage
5. Batches document indexing for better performance with large datasets
6. Saves the vector database to disk so it persists across Colab sessions

After installing the requirements, run the cells in the notebook to index the documents, instantiate the conversational agent, and it should be ready for questions. 
The chat_setup.py script provides a simple chat UI using ipywidgets.


This project was created as a way to learn more about conversational AI and gain hands-on experience with LangChain.
