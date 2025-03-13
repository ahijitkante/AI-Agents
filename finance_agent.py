import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class FinanceAgent:
    def __init__(self):
        self.agent = Agent(
            name="Finance Agent",
            description="Your task is to find finance information",
            model=Groq(id="llama-3.3-70b-versatile"),
            tools=[
                YFinanceTools(
                    stock_price=True,
                    analyst_recommendations=True,
                    company_info=True,
                    company_news=True
                )
            ],
            instructions=["Use tables to display data"],
            show_tool_calls=True,
            markdown=True,
            debug_mode=True
        )

    def handle_query(self, query):
        return self.agent.run(query).content
