"""
A World of Countries - Continents methods test suite

A list of individual tests to perform to check the correct
functionalities of the AWOC class methods about continents.

"""

# Import pytest
import pytest

# Import the A World of Countries Python Module.
import awoc

# Creating a global fixture for serving the main AWOC class instance to all running tests.
@pytest.fixture
def awoc_class():

    # Initializing and returning an AWOC class instance.
    return awoc.AWOC()


class TestClass:
    # 1. get_continents_list()
    def test_get_continents_list(self, awoc_class):

        # Fetching results.
        continents_list = awoc_class.get_continents_list()

        # Asserting the result is a list.
        assert (continents_list is not False and isinstance(
            continents_list, list))

    # 2. get_continents()
    def test_get_continents(self, awoc_class):

        # Fetching results.
        continents_data = awoc_class.get_continents()

        # Asserting the result is a list.
        assert (continents_data is not False and isinstance(
            continents_data, list))

        # Asserting the result is a list of dictionaries.
        for c in continents_data:
            assert isinstance(c, dict)
