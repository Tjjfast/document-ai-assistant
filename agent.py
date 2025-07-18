from agno.agent import Agent
from agno.models.google import Gemini
from agno.storage.sqlite import SqliteStorage
from knowledgebase import knowledge_base

import os
from dotenv import load_dotenv 

load_dotenv() 


instructions = [
"You are a Thai cooking assistant with access to a Thai recipe database.",
"Always search your knowledge base first before responding.",
"You only answer with recipes from your database."
"You don't use your internal knowledge."
"If you can't answer with the database, simple return 'I don't know'",
]

agent = Agent(
    model=Gemini(id='gemini-1.5-flash', api_key=os.getenv('GOOGLE_API_KEY')),
    knowledge=knowledge_base,
    search_knowledge=True,
    storage=SqliteStorage(db_file="agent.db", table_name="sessions"), 
    show_tool_calls=True,         
    markdown=True,  
    instructions=instructions,
)


agent.cli_app(stream=False)
