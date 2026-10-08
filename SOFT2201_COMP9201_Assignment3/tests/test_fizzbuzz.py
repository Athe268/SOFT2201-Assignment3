# Record coverage of the unmodified starter suite before extending the tests.
# ORIGINAL statement coverage: ____%
# ORIGINAL branch coverage: ____%
# Use one decimal place.

# Q4: Coverage subsumption
# Include the program, test suite, and explanation as comments.
# Answer: 

from quiz_platform.examples.fizzbuzz import fizzbuzz


def test_generates_first_two_values():
    assert fizzbuzz(2) == ["1", "2"]

# FILL IN: Add more tests to achieve 100% statement and branch coverage of fizzbuzz.py.