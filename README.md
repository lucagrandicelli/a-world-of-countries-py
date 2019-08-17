# A World of Countries

![](images/awoc-cover.jpg)
A World of Countries (AWOC) is a fully-featured library that provides an easy layer to access mutiple data about world continents and countries, according to the ISO Standard 3166-1.

**Note:** A NodeJS version of this library is available [here](https://github.com/lucagrandicelli/a-world-of-countries/)

## Installation

```
$ pip install a-world-of-countries
```

## How to use the AWOC library

```python
# Import the AWOC package.
import awoc

# Initialize the AWOC class.
my_world = awoc.AWOC()

# Let's retrieve the full list of nations of Europe.
countries_of_europe = my_world.get_countries_list_of('Europe')
# It returns: [ 'Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', and so on... ]

# We can get the whole country data as well.
italy_data = my_world.get_country_data('Italy')
"""
Returns:
{
  'Country Name': 'Italy',
  ISO2: 'IT',
  ISO3: 'ITA',
  TLD: 'it',
  FIPS: 'IT',
  'ISO Numeric': '380',
  GeoNameID: '3175395',
  E164: '39',
  'Phone Code': '39',
  'Continent Name': 'Europe',
  'Continent Code': 'eu',
  Capital: 'Rome',
  'Time Zone in Capital': 'Europe/Rome',
  'Currency Name': 'Euro',
  Languages:
   'Italian (official), German (parts of Trentino-Alto Adige region are predominantly German-speaking), French (small French-speaking minority in Valle d\'Aosta region), Slovene (Slovene-speaking minority in the Trieste-Gorizia area)',
  'Area KM2': '301230'
}
"""
```

## How it works

A World of Countries is a library based upon a world.json file which holds all the continents and countries informations we need. The file is ntly evolving and this library, encoded in the form of a JS class, exposes a list of methods you can use to access those data without the hassle of writing data extraction code.

In the `data/world.json` (known as Global World Data Object, GWDO) file, every country is encoded as an object /w the following properties:

- **Country Name** - Full name of the country. E.g. "Italy".
- **ISO2** - ISO2/3166-1 alpha-2 country code. E.g. "IT"
- **ISO3** - ISO2/3166-1 alpha-2 country code. E.g. "ITA"
- **TLD** - Top Level Domain code. E.g. "it"
- **FIPS** - Federal Information Processing Standards (FIPS) code. E.g. "IT"
- **ISO Numeric** - ISO 3166-1 numeric code. E.g. "380"
- **GeoNameID** - GEO Name ID. E.g. "3175395"
- **E164** - International Public Telecommunication Numbering Plan Code. E.g. "39"
- **Phone Code**- Country phone code. E.g. "39"
- **Continent Name** - Full name of the continent the country belongs to. E.g. "Europe"
- **Continent Code** - Continent code the country belongs to. E.g. "eu"
- **Capital** - Country capital city. E.g. "Rome"
- **Time Zone in Capital** - Full definition of the country time zone. E.g. "Europe/Rome"
- **Currency Name** - Full currency name. E.g. "Euro"
- **Languages** - A verbose list of spoken languages. E.g. "Italian (official), German (parts of Trentino-Alto Adige region are predominantly German-speaking), French (small French-speaking minority in Valle d'Aosta region), Slovene (Slovene-speaking minority in the Trieste-Gorizia area)"
- **Area KM2** - Geographic extension area in km2/mi2. E.g. "301230"

## AWOC Available Methods

The whole library code is heavily commented, so every class property or method exposes a verbose explanation of its purpose. Feel free to inspect the code and find you preferred method of work. The following is the updated list of all AWOC available methods.

## WORLD CONTINENTS

_List of all AWOC.js methods about world continents._

### get_continents_list()

**Description**: returns a list of continent names as strings.

```python
# Let's fetch a list of all continents of planet Earth.
continents_list = my_world.get_continents_list()
# Returns: ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
```

### get_continents()

**Description**: returns a list of continent objects.

```python
# Let's fetch a list of all continents of planet Earth in form of data objects.
continents_data = my_world.get_continents()
"""
 Returns:
 [
  { 'Continent Code': 'af', 'Continent Name': 'Africa' },
  { 'Continent Code': 'an', 'Continent Name': 'Antarctica' },
  { 'Continent Code': 'as', 'Continent Name': 'Asia' },
  { 'Continent Code': 'eu', 'Continent Name': 'Europe' },
  { 'Continent Code': 'na', 'Continent Name': 'North America' },
  { 'Continent Code': 'oc', 'Continent Name': 'Oceania' },
  { 'Continent Code': 'sa', 'Continent Name': 'South America' }
 ]
"""
```

## WORLD COUNTRIES

### get_countries()

**Description**: This method extracts all the countries data from the GWOD. It performs an additional sort by country name to ensure the correct alphabetical order, regardless of the GWOD json objects order (which might fail).

```python
# Let's fetch the data of all countries of the world.
countries = my_world.get_countries()
"""
 Returns the full list of country objects.
 [...
 { 'Country Name': 'Cocos Islands', ISO2: 'CC', ISO3: 'CCK', TLD: 'cc', .. },
 { 'Country Name': 'Colombia', ISO2: 'CO', ISO3: 'COL', TLD: 'co', ... },
 ... ]
"""
```

### get_country_data(country_name, field = false)

**Description**: this method returns a single country object data. If a `field` parameter is specified, then the method will return its value. For a list of available fields, please check the country data structure above.

```python
# We can fetch a single value from the country data object.
capital_of_spain = my_world.get_country_data('Spain', 'Capital')
# Returns: "Madrid".

# ... or just the full object.
spain_data = my_world.get_country_data('Spain')
# Returns: {'Country Name': 'Spain', ISO2: 'ES', ISO3: 'ESP', TLD: 'es', ... }
```

### get_countries_list()

**Description**: this method returns a list of country names sorted alphabetically.

```python
# Let's fetch a list of world nations.
get_countries_list = my_world.get_countries_list()
# Returns: ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', ...]
```

### get_countries_list_of(continent_name)

**Description**: this method returns a list of country names sorted alphabetically for a specific continent.

```python
# Let's fetch the list of nations of Europe.
nations_of_europe = my_world.get_countries_list_of('Europe')
# Returns: [ 'Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', ...]
```

### get_countries_data_of(continent_name)

**Description**: this method returns a list of country objects alphabetically sorted per each country name for a specific continent.

```python
# Let's fetch the list of nations of Europe in form of country objects.
nations_of_europe = my_world.get_countries_data_of('Europe')
"""
 Returns:
 [
  { 'Country Name': 'Albania', ISO2: 'AL', ISO3: 'ALB', ... },
  { 'Country Name': 'Andorra', ISO2: 'AD', ISO3: 'AND', ... }
 ]
"""
```

### get_country_ISO2(country_name)

**Description**: this method returns the ISO2 code for the specified country.

```python
italy_ISO2 = my_world.get_country_ISO2('Italy')
# Returns: 'IT'
```

### get_country_ISO3(country_name)

**Description**: this method returns the ISO3 code for the specified country.

```python
italy_ISO3 = my_world.get_country_ISO3('Italy')
# Returns: 'ITA'
```

### get_country_TLD(country_name)

**Description**: this method returns the Top Level Domain (TLD) for the specified country.

```python
italy_TLD = my_world.get_country_TLD('Italy')
# Returns: 'it'
```

### get_country_FIPS(country_name)

**Description**: this method returns the FIPS country code for the specified country.

```python
italy_FIPS = my_world.get_country_FIPS('Italy')
# Returns: 'IT'
```

### get_country_ISO_numeric(country_name)

**Description**: this method returns the ISO Numeric code for the specified country.

```python
italy_ISO_numeric = my_world.get_country_ISO_numeric('Italy')
# Returns: '380'
```

### get_country_geo_name_ID(country_name)

**Description**: this method returns the GEO Name ID for the specified country.

```python
italy_GEO_name_ID = my_world.get_country_geo_name_ID('Italy')
# Returns: '3175395'
```

### get_country_E164(country_name)

**Description**: this method returns the E164 code for the specified country.

```python
italy_E164 = my_world.get_country_E164('Italy')
# Returns: '39'
```

### get_country_phone_code(country_name)

**Description**: this method returns the Phone Code for the specified country.

```python
italy_phone_code = my_world.get_country_phone_code('Italy')
# Returns: '39'
```

### get_country_continent_name(country_name)

**Description**: this method returns the continent data the specified country belongs to.

```python
italy_continent_name = my_world.get_country_continent_name('Italy')
# Returns: 'Europe'
```

### get_country_continent_code(country_name)

**Description**: this method returns the continent code the specified country belongs to.

```python
italy_continent_code = my_world.get_country_continent_code('Italy')
# Returns: 'eu'
```

### get_country_capital_city(country_name)

**Description**: this method returns the capital city of the specified country.

```python
capital_of_italy = my_world.get_country_capital_city('Italy')
# Returns: 'Rome'
```

### get_country_time_zone(country_name)

**Description**: this method returns a time zone value for the specific country.

```python
italy_time_zone = my_world.get_country_time_zone('Italy')
# Returns: 'Europe/Rome'
```

### get_country_currency_name(country_name)

**Description**: this method returns the currency name for the specified country.

```python
italy_currency_name = my_world.get_country_currency_name('Italy')
# Returns: 'Euro'
```

### get_countries_list_by_currency(currency_name, continent_name = false)

**Description**: this method returns a list of country names filtered by a specific currency.

```python
# Let's fetch all the countries where the dollar is used.
dollar_nations = my_world.get_countries_list_by_currency('Dollar')
# Returns: [ 'American Samoa', 'Anguilla', 'Antigua and Barbuda', 'Australia', 'Bahamas', ... ]

# We can also filter the above by continent.
dollar_nations_in_south_america = my_world.get_countries_list_by_currency(
  'Dollar',
  'South America'
)
# Returns: [ 'Ecuador', 'Guyana', 'Suriname' ]
```

### get_countries_data_by_currency(currency_name, continent_name = false)

**Description**: this method returns one or multiple country object data for a specific currency.

```python
# Let's fetch all the countries where the dollar is used in form of data objects
dollar_nations_obj = my_world.get_countries_data_by_currency('Dollar')
"""
 Returns:
 [...
  { 'Country Name': 'American Samoa', ISO2: 'AS', ISO3: 'ASM', TLD: 'as', FIPS: 'AQ', ... },
  { 'Country Name': 'Anguilla', ISO2: 'AI', ISO3: 'AIA', TLD: 'ai', FIPS: 'AV', ... },
 ...]
"""

# We can also filter the above by continent.
dollar_nations_in_south_americaObj = my_world.get_countries_data_by_currency(
  'Dollar',
  'South America'
)
"""
 Returns:
 [
   { 'Country Name': 'Ecuador', ISO2: 'EC', ISO3: 'ECU', TLD: 'ec', FIPS: 'EC', ... },
   { 'Country Name': 'Guyana',  ISO2: 'GY', ISO3: 'GUY', TLD: 'gy', FIPS: 'GY', ... },
   { 'Country Name': 'Suriname', ISO2: 'SR', ISO3: 'SUR', TLD: 'sr', FIPS: 'NS', ... }
 ]
 """
```

### get_country_languages(country_name)

**Description**: this method returns a list of languages for the specific country.

```python
italy_language_codes = my_world.get_country_languages('Italy')
# Returns: 'Italian (official)', 'German (parts of Trentino-Alto Adige region are predominantly German-speaking)', 'French (small French-speaking minority in Valle d\'Aosta region)', 'Slovene (Slovene-speaking minority in the Trieste-Gorizia area)'.
```

### get_country_area(country_name, unit = 'km2')

**Description**: this method returns the country area in km2 or mi2.

```python
# Let's fetch the extension area of Italy in km2
italy_extension_area_km2 = my_world.get_country_area('Italy')
# Returns: 301230

# We can fetch it in mi2 too.
italy_extension_area_mi2 = my_world.get_country_area('Italy', 'mi2')
# Returns: 116305.44
```

## Changelog

### 1.0.0

Initial release.

## Licence

[MIT](https:#github.com/lucagrandicelli/a-world-of-countries-py/blob/master/LICENSE)

## Credits

- Cover image by [freepik](https:#it.freepik.com/foto-vettori-gratuito/viaggio).
