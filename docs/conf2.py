# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Python GIS Tutorials'
copyright = '2023, Hugh Semple'
author = 'Hugh Semple'
release = '0.0.0.1'

# -- General configuration ---------------------------------------------------
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_book_theme'
html_theme_options = {
    'repository_url': 'https://github.com/username/repository',
    'repository_branch': 'main',
    'path_to_docs': 'docs',
}

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
