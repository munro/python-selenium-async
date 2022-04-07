import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath(".."))

project = "selenium_async"
copyright_year = "-".join(str(x) for x in {2022, date.today().year})
copyright = f"{copyright_year}, Ryan Munro"
author = "Ryan Munro"
release = "0.1.0"
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
templates_path = []
exclude_patterns = []
html_theme = "sphinx_rtd_theme"
html_static_path = []
