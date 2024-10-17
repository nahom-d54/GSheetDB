from setuptools import setup, find_packages

setup(
    name="GSheetDB",
    version="1.0.0",
    description="A PyMongo-inspired Google Sheets library for Python",
    author="Nahom Dereje",
    author_email="nahom@nahom.eu.org",
    url="https://github.com/nahom-d54/gsheetdb",
    packages=find_packages(),
    install_requires=[
        "gspread>=5.7.0", 
        "google-auth>=2.20.0",
        "pandas>=1.3.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "gsheetdb-cli=gsheetdb.cli:cli",
        ]
    },
)
