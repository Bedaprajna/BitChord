from app.core.model import LocalLLM
from app.core.state import BitChordState


class SummarizerAgent:
    """
    Summarization and final-response agent.
    """

    def __init__(self, llm: LocalLLM):
        self.llm = llm

    async def run(self, state: BitChordState) -> str:
        previous_results = "\n\n".join(state.results)

        prompt = f"""
You are the Summarizer Agent in an AI orchestration system.

Original user request:
{state.user_input}

Previous agent results:
{previous_results}

Create a clear, concise final response for the user.
Use the previous results as context and do not invent unsupported information.
"""

        result = self.llm.generate(
            prompt,
            max_tokens=400,
            temperature=0.2,
        )

        state.final_response = result
        state.add_result(result)
        state.mark_completed("summarizer")

        return result
