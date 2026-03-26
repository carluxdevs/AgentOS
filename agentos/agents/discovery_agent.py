from agentos.core.base_agent import BasePOMAgent
from agentos.tools.mock_tools import build_opportunity_solution_tree

class DiscoveryAgent(BasePOMAgent):
    def __init__(self):
        super().__init__(
            agent_id="product-discovery",
            md_file_path="data/agents/discovery_agent.md",
            tool_implementations={
                "build_opportunity_solution_tree": build_opportunity_solution_tree
            }
        )
