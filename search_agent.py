import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SearchAgent:
    def __init__(self):
        self.agent = Agent(
            name="Web Agent",
            description="Agent for searching content from the web",
            model=Groq(id="mixtral-8x7b-32768"),
            tools=[DuckDuckGo()],
            instructions="Always include the sources.",
        )

    def handle_query(self, query):
        return self.agent.run(query).content
