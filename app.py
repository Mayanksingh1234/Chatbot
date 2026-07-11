import langchain
# from langchain_google_genai import ChatGoogleGenerativeAI
import llm as llm
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from memory import MemoryManager
store={}

# def get_session_history(session_id:str):
#     if session_id not in store:
#         store[session_id]=InMemoryChatMessageHistory()
#     # print(f"session history: {session_id}: {store[session_id]}")
#     return store[session_id]



chatbot_with_memory=MemoryManager()
while True:
    question=input("You: ")
    if question.lower()=="exit":
        break
    chatbot_with_memory.add_message_user(question)
    prompt=f""" you are a helpful assistant, you will get the previous conversation
    between user and ai {chatbot_with_memory.retrive_message()} 
    respont to the user latest question"""
    response=llm.llm.invoke(prompt)
    chatbot_with_memory.add_message_ai(response.content)
    print("Ans.: ",response.content)
data=chatbot_with_memory.summarize()
print(data)