from app.core.model import LocalLLM
from app.core.state import BitChordState


class ResearcherAgent:
    """
    Research-oriented agent.
    """

    def __init__(self, llm: LocalLLM):
        self.llm = llm

    async def run(self, state: BitChordState) -> str:
        prompt = f"""
You are the Researcher Agent in an AI orchestration system.

User request:
{state.user_input}

Provide a clear, factual and concise analysis.
Do not invent sources or facts.
"""

        result = self.llm.generate(
            prompt,
            max_tokens=300,
            temperature=0.2,
        )

        state.add_result(result)
        state.mark_completed("researcher")

        return result
