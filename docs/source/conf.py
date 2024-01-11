# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Add the directory containing the Python file to sys.path
sys.path.insert(0, os.path.abspath('/home/ashok/hosting_sample'))

project = 'Sample'
copyright = '2024, Anjanay'
author = 'Anjanay'
release = '1.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'abcd.rst', 'xyz.rst']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'special-members': True,
    'show-inheritance': True,
}

# Link to the GitHub repository
html_context = {
    'display_github': True,
    'github_user': 'your_github_user',
    'github_repo': 'your_repo_name',
    'github_version': 'main/',
    'github_url': 'https://github.com/harnalashok/catEncodersProject',
}
