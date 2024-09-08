import sys
import asyncio
from datetime import datetime
from graphiti_core import Graphiti
from graphiti_core.llm_client.groq_client import GroqClient
from graphiti_core.nodes import EpisodeType

# Add the path to your graphiti module
sys.path.append('/Users/viraatd/Documents/Personal/graphiti')

# Initialize the LLM client
llm_client = GroqClient()

# Initialize Graphiti
graphiti = Graphiti("bolt://localhost:7687", "neo4j", "password", llm_client=llm_client)

async def main():
    # Build indices and constraints
    await graphiti.build_indices_and_constraints()

    # Add episodes
    episodes = [
        "Kamala Harris is the Attorney General of California. She was previously "
        "the district attorney for San Francisco.",
        "As AG, Harris was in office from January 3, 2011 – January 3, 2017",
    ]
    for i, episode in enumerate(episodes):
        await graphiti.add_episode(
            name=f"Freakonomics Radio {i}",
            episode_body=episode,
            source=EpisodeType.text,
            source_description="podcast",
            reference_time=datetime.now()
        )

    # After adding episodes, you can check the database state
    all_edges = await graphiti.get_all_edges()  # Assuming you have a method to retrieve all edges
    print("All edges in the database:", all_edges)
    # Search the graph
    results = await graphiti.search('Who was the California Attorney General?')
    
    # Print results
    if results:
        for result in results:
            print(result)
    else:
        print("No results found.")

if __name__ == "__main__":
    asyncio.run(main())