"""Provides composite aggregation and rendering of quiz results.

Requires 0 <= earned <= possible and possible > 0 for each question.
Sections must form an acyclic tree and may be empty.
"""
from abc import ABC, abstractmethod


class ResultNode(ABC):
    @abstractmethod
    def totals(self) -> tuple[float, float]:
        """Returns earned and possible marks as a tuple."""

    @abstractmethod
    def __str__(self) -> str:
        """Returns the text representation of this result node."""


class QuestionResult(ResultNode):
    def __init__(self, earned: float, possible: float):
        self.earned = earned
        self.possible = possible

    def totals(self) -> tuple[float, float]:
        return (self.earned, self.possible)

    def __str__(self) -> str:
        """Returns marks in earned/possible format."""
        return f"{self.earned}/{self.possible}"


class QuizSection(ResultNode):
    """Aggregates results from child questions and nested sections."""
    def __init__(self, children):
        self.children = tuple(children)

    def totals(self) -> tuple[float, float]:
        values = [child.totals() for child in self.children]
        earned = sum(value[0] for value in values)
        possible = sum(value[1] for value in values)
        return (earned, possible)

    def __str__(self) -> str:
        """Returns comma-separated child representations enclosed in brackets."""
        return "[" + ", ".join(str(child) for child in self.children) + "]"


def summarise(node: ResultNode) -> dict:
    """Returns aggregate marks and percentage (None for zero possible marks)."""
    earned, possible = node.totals()
    if possible == 0:
        percentage = None
    else:
        percentage = earned * 100 / possible
    return {"earned": earned, "possible": possible, "percentage": percentage}
