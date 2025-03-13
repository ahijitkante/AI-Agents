import logging
from search_agent import SearchAgent
from finance_agent import FinanceAgent

# Suppress debug logs
logging.basicConfig(level=logging.WARNING)

class MasterAgent:
    def __init__(self):
        self.agents = {
            "search": SearchAgent(),
            "finance": FinanceAgent()
        }

    def route_query(self, agent_type, query):
        agent = self.agents.get(agent_type)
        if agent:
            return agent.handle_query(query)
        return "Invalid agent type!"

if __name__ == "__main__":
    master = MasterAgent()
    
    while True:
        print("\nAvailable agents: [search, finance]")
        agent_type = input("Select an agent (or type 'exit' to quit): ").strip().lower()

        if agent_type == "exit":
            print("Exiting...")
            break
        if agent_type not in master.agents:
            print("Invalid agent. Please choose 'search' or 'finance'.")
            continue
        
        query = input("Enter your query: ").strip()
        response = master.route_query(agent_type, query)
        
        print("\nResponse:", response)
