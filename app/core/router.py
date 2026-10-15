from app.core.state import BitChordState


class TaskRouter:
    """
    Dynamically decides which agent should handle a task.
    """

    def route(self, state: BitChordState) -> str:
        text = state.user_input.lower()

        if any(
            keyword in text
            for keyword in [
                "code",
                "python",
                "program",
                "debug",
                "bug",
                "function",
                "script",
            ]
        ):
            return "coder"

        if any(
            keyword in text
            for keyword in [
                "research",
                "find",
                "explain",
                "information",
                "analyze",
                "compare",
            ]
        ):
            return "researcher"

        return "summarizer"
