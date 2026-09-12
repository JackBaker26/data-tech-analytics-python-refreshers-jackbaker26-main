import pytest
import numpy as np
from testbook import testbook


@pytest.fixture(scope="module")
def tb():
    with testbook("./python-exercises.ipynb", execute=True) as tb:
        yield tb

def test_exercise2_1(tb):
    get_full_names = tb.ref("get_full_names")
# Test 3: For Extra Credit - Arrays of unequal lengths (This should raise an error)
    try:
        tb.inject("""
          unequal_first_names = np.array(["Bob"])
          unequal_last_names = np.array(["Smith", "Jones"])
        """)
        unequal_first_names = tb.ref("unequal_first_names")
        unequal_last_names = tb.ref("unequal_last_names")
        unequal_output = get_full_names(unequal_first_names, unequal_last_names)
        
    except ValueError:
        print("✅ Test 3 Passed! ValueError raised as expected.")
    except AssertionError as e:
        print(f"Test 3 Failed: {e}")
    except Exception as e:
        print(f"Test 3 Failed. Expected ValueError but got {type(e).__name__}: {e}")
    else:
        print("Test 3 Failed. No error was raised.")
