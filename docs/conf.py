# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python GIS Tutorials'
copyright = '2024, Hugh Semple'
author = 'Hugh Semple'
release = '0.0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Automatically document code
    'sphinx.ext.napoleon',  # Support for Google style and NumPy style docstrings
    # Add other extensions as needed
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import import pydata_sphinx_theme

html_theme = 'pydata_sphinx_theme'

# Optional: Customize theme options
html_theme_options = {
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# Optional: Specify the path to the theme
html_theme_path = [pydata_sphinx_theme.get_html_theme_path()]

# Optional: Specify static files (like CSS or JavaScript) if needed
html_static_path = ['_static']
