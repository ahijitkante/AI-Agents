from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[DuckDuckGo()],
    instructions="Always provide detailed analysis and include sources for information",
    debug_mode=True
)

def analyze_image_and_search(image_url: str, query: str):
    messages = [
        {"role": "system", "content": "You are an AI agent. Analyze images and provide responses."},
        {"role": "user", "content": f"Analyze the image at {image_url} and answer: {query}"}
    ]
    response = agent.run(messages=messages, stream=True)
    for chunk in response:
        print(chunk)

# Example usage
image_url = "https://en.wikipedia.org/wiki/File:Kiit_library_building.jpg"
query = "Tell me about the location and purpose of the building."
analyze_image_and_search(image_url, query)
