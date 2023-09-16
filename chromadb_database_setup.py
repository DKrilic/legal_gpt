from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
import chromadb

embeddings = OpenAIEmbeddings()
chroma_db_path = f'{root_dir}/database'
client = chromadb.PersistentClient(path=chroma_db_path)

# Check if the database already exists, if not create a new one
if not os.path.exists(chroma_db_path):
    vectordb = Chroma.from_documents(docs, client=client, embedding=embeddings)