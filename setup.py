import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="a-world-of-countries",
    version="1.0.0",
    author="Luca Grandicelli",
    author_email="luca.grandicelli79@gmail.com",
    description="A World of Countries (AWOC) is a fully-featured library that provides an easy layer to access mutiple data about world continents and countries, according to the ISO Standard 3166-1.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/lucagrandicelli/a-world-of-countries-py",
    packages=setuptools.find_packages(),
    install_requires=[
        'pydash',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ],
    keywords='geography countries countries-api geography-database world languages currency country country-names country-codes',
    include_package_data=True,
    zip_safe=False,
    test_suite="test"
)
