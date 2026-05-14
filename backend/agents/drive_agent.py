from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType

from backend.tools.drive_search_tool import search_drive

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

tools = [search_drive]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)