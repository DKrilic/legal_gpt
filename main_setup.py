from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
import time

embeddings = OpenAIEmbeddings()

chroma_db_path = f'{root_dir}/database_legal'
client = chromadb.PersistentClient(path=chroma_db_path)

collection_name = 'my_collection'

# Check if the collection already exists, if not create a new one
try:
    vectordb = client.get_collection(collection_name, embedding_function=embeddings)
except ValueError:
    client.create_collection(collection_name, embedding_function=embeddings)
    vectordb = client.get_collection(collection_name, embedding_function=embeddings)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# model params
llm = OpenAI(
    model_name="gpt-3.5-turbo-16k",
    temperature=0.9,
    top_p=0.95,
    max_tokens=2000
)

# batch params
batch_size = 1 
delay_time = 0.001 

# Splitting the documents into smaller batches, though this is a little finnicky. For PDFs with more than ~100 pages, I found it easier to manually split them up into multiple parts of ~100 pages each first. 
for i in range(0, len(docs), batch_size):
    batch_docs = docs[i:i+batch_size]
    vectordb = Chroma.from_documents(batch_docs, client=client, embedding=embeddings)
    time.sleep(delay_time)

pdf_qa = ConversationalRetrievalChain.from_llm(llm, vectordb.as_retriever(), memory=memory)