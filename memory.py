import llm as llm
class MemoryManager:
    def __init__(self):
        self.recent_messages=[]
        self.summary=""
        self.long_term_memory=[]
    def add_message_user(self, message: str):
        self.recent_messages.append(f"user: {message}")
    def add_message_ai(self, message: str):
        self.recent_messages.append(f"ai: {message}")
    def summarize(self):
        prompt=f"""
        You are a helpful assistant. Please summarize the following conversation between a user and an AI assistant. The summary should be concise and capture the main points of the conversation. {"\n".join(self.recent_messages)}"""
        summarize=llm.llm.invoke(prompt)
        self.summary=summarize.content
        return self.summary
    def retrive_message(self):
        return "\n".join(self.recent_messages)