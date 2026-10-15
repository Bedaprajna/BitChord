
from app.core.executor import BitChordExecutor
from app.core.state import BitChordState


def test_coder_execution_graph():
    executor = BitChordExecutor(llm=None)
    state = BitChordState(
        user_input="Write a Python function"
    )

    state.route = executor.router.route(state)

    assert executor._build_execution_graph(state) == [
        "coder",
        "summarizer",
    ]


def test_researcher_execution_graph():
    executor = BitChordExecutor(llm=None)
    state = BitChordState(
        user_input="Explain neural networks"
    )

    state.route = executor.router.route(state)

    assert executor._build_execution_graph(state) == [
        "researcher",
        "summarizer",
    ]


def test_summarizer_execution_graph():
    executor = BitChordExecutor(llm=None)
    state = BitChordState(
        user_input="Summarize this text"
    )

    state.route = executor.router.route(state)

    assert executor._build_execution_graph(state) == [
        "summarizer",
    ]
