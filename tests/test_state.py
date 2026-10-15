from app.core.state import BitChordState


def test_add_result():
    state = BitChordState(user_input="Test request")

    state.add_result("Test result")

    assert state.results == ["Test result"]


def test_mark_completed():
    state = BitChordState(user_input="Test request")

    state.mark_completed("coder")

    assert state.completed_steps == ["coder"]
    assert "coder" in state.step_timestamps


def test_execution_graph():
    state = BitChordState(user_input="Test request")

    state.set_execution_graph(["coder", "summarizer"])

    assert state.execution_graph == ["coder", "summarizer"]
