# Record coverage of the unmodified starter suite BEFORE extending the tests.
# ORIGINAL statement coverage: ____%
# Use one decimal place.

from quiz_platform.assessment_engine.quiz_results import QuestionResult, QuizSection, summarise


def test_one_question_section():
    section = QuizSection([QuestionResult(3, 4)])
    assert summarise(section) == {
        'earned': 3, 'possible': 4, 'percentage': 75.0,
    }


# FILL IN: Add more tests to achieve 100% statement and branch coverage of quiz_results.py. 
# Add more test functions to this file.
