# Testing code in python

# integration: checks if components works together
# unit: checks components individually
# Side effects are piece of code that could alter the environment such as filesystem
# or database
# Test runner is the python application that executes the test code.
# Fixture, is the data created as an input for the tests
# Parametrization, is when running the same test and passing it different values each time
# and expecting the same result

# Basic example with assert (wrap in function)
def basic_assert():
    # ok sample
    assert sum([1,2,3]) == 6, "Should be 6"
    # fail sample
    assert sum([1,2,3]) == 7, "Should be 7"


# Using Test Framework/Runner, python built in
# Needs to puts the tests into claseses and methods
import unittest
class TestingSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, "Should be 6")

    def test_sum_bad_value(self):
       # This test its ok if raises a TypeError
        value = "Not a valid sequence"
        with self.assertRaises(TypeError):
            result = sum(value)


# RUN TEST SAMPLES
if __name__ == "__main__":
    # basic_assert()
    # Running unittest
    unittest.main()