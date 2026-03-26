from agentos.core.base_agent import BasePOMAgent
from agentos.tools.mock_tools import manage_portfolio_roadmap, define_strategic_bets

class CPOAgent(BasePOMAgent):
    def __init__(self):
        super().__init__(
            agent_id="cpo_agent",
            md_file_path="data/agents/cpo_agent.md",
            tool_implementations={
                "manage_portfolio_roadmap": manage_portfolio_roadmap,
                "define_strategic_bets": define_strategic_bets,
            }
        )
