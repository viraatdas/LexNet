import sys
sys.path.append('/Users/viraatd/Documents/Personal/graphiti')

from graphiti_core import Graphiti
from graphiti_core.llm_client.groq_client import GroqClient
from graphiti_core.nodes import EpisodeType
from datetime import datetime
import asyncio
import dotenv


llm_client = GroqClient()

graphiti = Graphiti("bolt://localhost:7687", "neo4j", "password", llm_client=llm_client)

async def main():
    await graphiti.build_indices_and_constraints()

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

if __name__ == "__main__":
    asyncio.run(main())
