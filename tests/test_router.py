from app.core.router import TaskRouter
from app.core.state import BitChordState


def test_coder_route():
    state = BitChordState(
        user_input="Write a Python function to sort a list"
    )

    router = TaskRouter()

    assert router.route(state) == "coder"


def test_researcher_route():
    state = BitChordState(
        user_input="Explain how neural networks work"
    )

    router = TaskRouter()

    assert router.route(state) == "researcher"


def test_summarizer_route():
    state = BitChordState(
        user_input="Summarize this text"
    )

    router = TaskRouter()

    assert router.route(state) == "summarizer"
