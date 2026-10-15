from app.core.model import LocalLLM
from app.core.state import BitChordState


class CoderAgent:
    """
    Code-focused agent.
    """

    def __init__(self, llm: LocalLLM):
        self.llm = llm

    async def run(self, state: BitChordState) -> str:
        prompt = f"""
You are the Coder Agent in an AI orchestration system.

User request:
{state.user_input}

Provide a correct and concise programming solution.
Include code when appropriate.
Explain important parts briefly.
"""

        result = self.llm.generate(
            prompt,
            max_tokens=400,
            temperature=0.2,
        )

        state.add_result(result)
        state.mark_completed("coder")

        return result
