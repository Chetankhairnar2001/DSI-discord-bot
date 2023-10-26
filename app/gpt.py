from dotenv import load_dotenv

load_dotenv()

import os
import sys
import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
os.environ["OPENAI_API_KEY"] = os.getenv('CHATGPT_API_KEY')

# loader = TextLoader('data.txt')
loader = DirectoryLoader('./data', glob="**/*.txt", loader_cls=TextLoader, show_progress=True)
index = VectorstoreIndexCreator().from_loaders([loader])

def chatgpt_response(prompt):
    return index.query(prompt)

## earlier facing error in code below so commented u can try using the code since it could be more cost effective

# from dotenv import load_dotenv

# load_dotenv()
# import sys
# import os
# from langchain.document_loaders import TextLoader
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import Chroma
# from langchain.chat_models import ChatOpenAI
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.prompts import SystemMessagePromptTemplate, PromptTemplate
# os.environ["OPENAI_API_KEY"] = os.getenv('CHATGPT_API_KEY')

# loader = TextLoader('data.txt')
# documents = loader.load()
# # text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=100)
# # texts = text_splitter.split_documents(documents)
# # Create embeddings
# embeddings = OpenAIEmbeddings()
# retriever = Chroma.from_documents(documents, embeddings).as_retriever()
# chat = ChatOpenAI(temperature=0)
# prompt_template = """You are a helpful Discord bot that assists with questions about teaching or AI Camp.
# {context}
# Please provide a concise response using the provided data documents.
# Answer:"""

# prompt = PromptTemplate(
#     template=prompt_template, input_variables=["context"]
# )
# system_message_prompt = SystemMessagePromptTemplate(prompt=prompt)

# def chatgpt_response(prompt):
#     try:
#         # Generate a response using your AI model
#         context = retriever.get_relevant_documents(query=prompt)
#         formatted_prompt = system_message_prompt.format(context=context)
#         response = chat([formatted_prompt]).content
#         return response
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return "Sorry, I couldn't generate a response at the moment."
