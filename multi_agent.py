from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import time
from dotenv import load_dotenv

load_dotenv()

# Web Search Agent
web_search_agent = Agent(
    name="Web Agent",
    description="This agent searches content from the web.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions="Always include sources.",
    debug_mode=True
)

# Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    description="Finds finance-related information.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True
        )
    ],
    instructions="Use tables to display data.",
    debug_mode=True
)

# Multi-Agent Team
agent_team = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions="Always include sources. Use tables to display data.",
    debug_mode=True
)

def rate_limited_response(agent, query):
    """Runs the agent and prints the response while handling rate limits."""
    try:
        response = agent.run(message=query, stream=False)  # Run without streaming
        print("\n📌 Response:\n", response)  # Print the response
    except Exception as e:
        print(f"❌ Error: {e}")
        time.sleep(60)  # Wait 1 minute if rate limit exceeded
        response = agent.run(message=query, stream=False)
        print("\n📌 Response (after retry):\n", response)  # Print the response after retry

# Run the agents with a sample query
rate_limited_response(agent_team, "Summarize analyst recommendations and share the latest news for TSLA")
