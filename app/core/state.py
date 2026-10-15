from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class BitChordState:
    """
    Shared state passed between agents during execution.
    """

    user_input: str

    current_task: str = ""

    route: str = ""

    results: list[str] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    final_response: str = ""

    completed_steps: list[str] = field(default_factory=list)

    execution_graph: list[str] = field(default_factory=list)

    step_timestamps: dict[str, str] = field(default_factory=dict)

    def add_result(self, result: str) -> None:
        self.results.append(result)

    def mark_completed(self, step: str) -> None:
        self.completed_steps.append(step)
        self.step_timestamps[step] = datetime.now().isoformat()

    def set_execution_graph(self, graph: list[str]) -> None:
        self.execution_graph = graph
