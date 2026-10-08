# Record coverage of the unmodified starter suite BEFORE extending the tests.
# ORIGINAL branch coverage: ____%
# Use one decimal place.

from quiz_platform.assessment_engine.result_adapters import (
    Result, NativeResults, PercentageExport, PercentageAdapter,
    build_report,
)


def test_report_from_native_results():
    source = NativeResults([Result('Q-1', 3, 4)])
    assert build_report(source) == {
        'earned': 3, 'possible': 4, 'percentage': 75.0,
    }


# FILL IN: Add more tests to achieve 100% statement and branch coverage of result_adapters.py. 
# Add more test functions to this file
