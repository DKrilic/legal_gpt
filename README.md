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


This project was created as a way to learn more about conversational AI and gain hands-on experience with LangChain and embedded databases.

# Usage example 

I created a database out of "New Commentary on the Code of Canon Law (2000)" consisting of some 1900 pages. 
Below is a snippet from the text as an example. 

![pdf_snippet](https://github.com/DK-1995/legal_gpt/assets/145159719/14aed5d6-d328-4004-bbdc-e4c8c23f15cc)

Using GPT-4 as a reference, it does not seem to know of this specific text:
![default_gpt4](https://github.com/DK-1995/legal_gpt/assets/145159719/4d351dda-18a2-4343-911f-f0f6b5585e23)

Whereas the Langchain model can retrieve the correct specific information (though still editing it slightly): 
![embedded_gpt](https://github.com/DK-1995/legal_gpt/assets/145159719/d2d5f365-f15a-461e-aa29-729f1ad0b4f1)
