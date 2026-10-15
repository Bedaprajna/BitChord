from app.core.state import BitChordState
from app.core.router import TaskRouter
from app.core.model import LocalLLM

from app.agents.researcher import ResearcherAgent
from app.agents.coder import CoderAgent
from app.agents.summarizer import SummarizerAgent


class BitChordExecutor:
    """
    Async orchestration engine for BitChord.

    Supports:
    - Dynamic routing
    - Stateful execution
    - Sequential agent chains
    - Conditional graph execution
    - Async agent execution
    """

    def __init__(self, llm: LocalLLM):
        self.router = TaskRouter()

        self.agents = {
            "researcher": ResearcherAgent(llm),
            "coder": CoderAgent(llm),
            "summarizer": SummarizerAgent(llm),
        }

    def _build_execution_graph(self, state: BitChordState) -> list[str]:
        """
        Build the execution path dynamically based on the current state.

        This is the conditional graph used by BitChord.
        """

        if state.route == "coder":
            return [
                "coder",
                "summarizer",
            ]

        if state.route == "researcher":
            return [
                "researcher",
                "summarizer",
            ]

        return [
            "summarizer",
        ]

    async def run(self, user_input: str) -> BitChordState:
        """
        Execute a complete BitChord workflow.
        """

        # Create shared state.
        state = BitChordState(
            user_input=user_input
        )

        # Dynamically select the initial route.
        state.route = self.router.route(state)

        # Build the conditional execution graph.
        execution_graph = self._build_execution_graph(state)
        state.set_execution_graph(execution_graph)

        # Execute each node in the selected graph sequentially.
        for node in execution_graph:
            agent = self.agents[node]
            await agent.run(state)

        return state
