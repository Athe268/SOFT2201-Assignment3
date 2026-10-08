"""Demonstrates result aggregation and adapter integration."""
from quiz_platform.examples.fizzbuzz import fizzbuzz
from quiz_platform.assessment_engine.quiz_results import QuestionResult, QuizSection, summarise
from quiz_platform.assessment_engine.result_adapters import Result, NativeResults, PercentageExport, PercentageAdapter, build_report


def main():
    print("FizzBuzz:", fizzbuzz(15))
    section = QuizSection([QuestionResult(3, 4)])
    print("Section:", summarise(section))
    print("Section text:", str(section))
    native = NativeResults([Result("Q-1", 3, 4)])
    percentages = PercentageAdapter(PercentageExport({
        "questions": [{"id": "Q-1", "weight": 4}], "submissions": {"Q-1": 75}}))
    print("Existing native source:", build_report(native))
    print("New external source through adapter:", build_report(percentages))


if __name__ == "__main__":
    main()
