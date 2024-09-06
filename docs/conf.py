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

html_theme = 'alabaster'

# Add custom static files
html_static_path = ['_static']

# Add custom CSS file
html_css_files = [
    'custom.css',
]

# Optional: Customize theme options
html_theme_options = {
    'description': 'Introductory tutorials to get started with Python for GIS',
    'fixed_sidebar': True,
    'sidebar_collapse': True,
    'show_powered_by': False,
    # Add other options as needed
}

