"""
A World of Countries - Countries methods test suite

A list of individual tests to perform to check the correct
functionalities of the AWOC class methods about countries.

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
    # 1. get_countries()
    def test_get_countries(self, awoc_class):

        # Fetching results.
        countries_list = awoc_class.get_countries()

        # Asserting the result is a list.
        assert (countries_list is not False and isinstance(
            countries_list, list))

        # Asserting each item of the resulting list is a dictionary.
        for c in countries_list:
            assert isinstance(c, dict)

    # 2. get_countries_list()
    def test_get_countries_list(self, awoc_class):

        # Fetching results.
        countries_list = awoc_class.get_countries_list()

        # Asserting the result is a list.
        assert (countries_list is not False and isinstance(
            countries_list, list))

    # 3. get_country_data(country_name)
    def test_get_country_data(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_data()

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_data = awoc_class.get_country_data(c)

            # Asserting the result is a list.
            assert (country_data is not False and isinstance(
                country_data, dict))

    # 4. get_countries_list_of(continent_name)
    def test_get_countries_list_of(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_countries_list_of()

        # Looping through countries.
        for c in awoc_class.get_continents_list():

            # Fetching results.
            country_list = awoc_class.get_countries_list_of(c)

            # Asserting the result is a list.
            assert (country_list is not False and isinstance(
                country_list, list))

    # 5. get_countries_data_of(continent_name)
    def test_get_countries_data_of(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_countries_data_of()

        # Looping through countries.
        for c in awoc_class.get_continents_list():

            # Fetching results.
            countries_data = awoc_class.get_countries_data_of(c)

            # Asserting the result is a list.
            assert (countries_data is not False and isinstance(
                countries_data, list))

            # Asserting each list item is a dictionary.
            for cd in countries_data:
                assert isinstance(cd, dict)

    # 6. get_country_ISO2(country_name)
    def test_get_country_ISO2(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_ISO2() and awoc_class.get_country_ISO2('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_ISO2 = awoc_class.get_country_ISO2(c)

            # Asserting each result is a string.
            assert isinstance(country_ISO2, str)

    # 7. get_country_ISO3(country_name)
    def test_get_country_ISO3(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_ISO3() and awoc_class.get_country_ISO3('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_ISO3 = awoc_class.get_country_ISO3(c)

            # Asserting each result is a string.
            assert isinstance(country_ISO3, str)

    # 8. get_country_TLD(country_name)
    def test_get_country_TLD(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_TLD() and awoc_class.get_country_TLD('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_TLD = awoc_class.get_country_TLD(c)

            # Asserting each result is a string.
            assert isinstance(country_TLD, str)

    # 9. get_country_TLD(country_name)
    def test_get_country_FIPS(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_FIPS() and awoc_class.get_country_FIPS('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_FIPS = awoc_class.get_country_FIPS(c)

            # Asserting each result is a string.
            assert isinstance(country_FIPS, str)

    # 10. get_country_TLD(country_name)
    def test_get_country_ISO_numeric(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_ISO_numeric(
            ) and awoc_class.get_country_ISO_numeric('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_ISO_numeric = awoc_class.get_country_ISO_numeric(c)

            # Asserting each result is a string.
            assert isinstance(country_ISO_numeric, str)

    # 11. get_country_TLD(country_name)
    def test_get_country_geo_name_ID(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_geo_name_ID(
            ) and awoc_class.get_country_geo_name_ID('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_geo_name_ID = awoc_class.get_country_geo_name_ID(c)

            # Asserting each result is a string.
            assert isinstance(country_geo_name_ID, str)

    # 12. get_country_TLD(country_name)
    def test_get_country_E164(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_E164(
            ) and awoc_class.get_country_E164('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_E164 = awoc_class.get_country_E164(c)

            # Asserting each result is a string.
            assert isinstance(country_E164, str)

    # 13. get_country_TLD(country_name)
    def test_get_country_phone_code(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_phone_code(
            ) and awoc_class.get_country_phone_code('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_phone_code = awoc_class.get_country_phone_code(c)

            # Asserting each result is a string.
            assert isinstance(country_phone_code, str)

    # 14. get_country_TLD(country_name)
    def test_get_country_continent_name(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_continent_name(
            ) and awoc_class.get_country_continent_name('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_continent_name = awoc_class.get_country_continent_name(c)

            # Asserting each result is a string.
            assert isinstance(country_continent_name, str)

    # 15. get_country_TLD(country_name)
    def test_get_country_continent_code(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_continent_code(
            ) and awoc_class.get_country_continent_code('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_continent_code = awoc_class.get_country_continent_code(c)

            # Asserting each result is a string.
            assert isinstance(country_continent_code, str)

    # 16. get_country_TLD(country_name)
    def test_get_country_capital_city(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_capital_city(
            ) and awoc_class.get_country_capital_city('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_capital_city = awoc_class.get_country_capital_city(c)

            # Asserting each result is a string.
            assert isinstance(country_capital_city, str)

    # 17. get_country_TLD(country_name)
    def test_get_country_time_zone(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_time_zone(
            ) and awoc_class.get_country_time_zone('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_time_zone = awoc_class.get_country_time_zone(c)

            # Asserting each result is a string.
            assert isinstance(country_time_zone, str)

    # 18. get_country_TLD(country_name)
    def test_get_country_currency_name(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_currency_name(
            ) and awoc_class.get_country_currency_name('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_currency_name = awoc_class.get_country_currency_name(c)

            # Asserting each result is a string.
            assert isinstance(country_currency_name, str)

    # 19. get_countries_list_by_currency(currency_name, continent_name=False)
    def test_get_countries_list_by_currency(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_countries_list_by_currency(
            ) and awoc_class.get_countries_list_by_currency('wrong parameter')

            # Fetching results.
            countries_list = awoc_class.get_countries_list_by_currency(
                'Dollar', 'North America')

            # Asserting each result is a list of strings.
            assert isinstance(countries_list, list)
            for c in countries_list:
                assert isinstance(c, str)

    # 20. get_countries_data_by_currency(currency_name, continent_name=False)
    def test_get_countries_data_by_currency(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_countries_data_by_currency(
            ) and awoc_class.get_countries_data_by_currency('wrong parameter')

            # Fetching results.
            countries_data = awoc_class.get_countries_data_by_currency(
                'Dollar', 'North America')

            # Asserting each result isdata of strings.
            assert isinstance(countries_data, list)
            for c in countries_data:
                assert isinstance(c, dict)

    # 21. get_country_languages(country_name)
    def test_get_country_languages(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_languages(
            ) and awoc_class.get_country_languages('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_languages = awoc_class.get_country_languages(c)

            # Asserting each result is a string.
            assert isinstance(country_languages, str)

    # 22. get_country_area(country_name, unit = 'km2')
    def test_get_country_area(self, awoc_class):

        # Testing exceptions.
        with pytest.raises(Exception):
            assert awoc_class.get_country_area(
            ) and awoc_class.get_country_area('wrong parameter')

        # Looping through countries.
        for c in awoc_class.get_countries_list():

            # Fetching results.
            country_area = awoc_class.get_country_area(c)

            # Asserting each result is a string.
            assert isinstance(country_area, float)
