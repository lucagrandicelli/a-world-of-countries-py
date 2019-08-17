"""
A World of Countries - world.json (GWDO) test suite

A list of individual tests to perform to check the correct
functionalities of the AWOC class methods about countries.

"""

# Import the standard library os path module.
import os.path

# Import json module.
import json

# Absolute dir the script is in
script_dir = os.path.dirname(__file__)

# The path to the Global World Object Data file.
relative_GWOD_path = '../awoc/data/world.json'

# Building GWOD full relative path.
GWOD_path = os.path.join(script_dir, relative_GWOD_path)


# Testing if the GWOD json file exists.
def test_gwod_exists():

    # Make sure our GWOD exists.
    assert os.path.exists(GWOD_path)


# Testing the GWOD as a valid json schema.
def test_validate_gwod():

    # Loading GWOD json file.
    with open(GWOD_path, "r") as json_file:
        json.load(json_file)
