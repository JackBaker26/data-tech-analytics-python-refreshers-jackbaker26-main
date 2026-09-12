import pytest
import numpy as np
from testbook import testbook


@pytest.fixture(scope="module")
def tb():
    with testbook("./python-exercises.ipynb", execute=True) as tb:
        yield tb

def test_exercise2_1(tb):
    get_full_names = tb.ref("get_full_names")
    # Test 1: Basic functionality
    try:
        tb.inject("""
            sample_first_names = np.array(["Bob", "Jane", "Mallory"])
            sample_last_names = np.array(["Smith", "Jones", "Williams"])
        """)
        sample_first_names = tb.ref("sample_first_names")
        sample_last_names = tb.ref("sample_last_names")
        expected_output = np.array(["Bob Smith", "Jane Jones", "Mallory Williams"])
        output = get_full_names(sample_first_names, sample_last_names)

        assert np.array_equal(output, expected_output), f"Expected {expected_output}, but got {output}"
        
    except AssertionError as e:
        print(f"Test 1 Failed: {e}")
    else:
        print("Test 1 Passed!")

def test_exercise2_2(tb):
    get_full_names = tb.ref("get_full_names")
    # Test 2: Empty strings or arrays
    try:
        tb.inject("""
            empty_first_names = np.array(["", "Jane", ""])
            empty_last_names = np.array(["Smith", "", "Williams"])
        """)
        empty_first_names = tb.ref("empty_first_names")
        empty_last_names = tb.ref("empty_last_names")
        expected_empty_output = np.array([" Smith", "Jane ", " Williams"])
        empty_output = get_full_names(empty_first_names, empty_last_names)

        assert np.array_equal(empty_output, expected_empty_output), f"Expected {expected_empty_output}, but got {empty_output}"

    except AssertionError as e:
        print(f"Test 2 Failed: {e}")
    else:
        print("✅ Test 2 Passed!")