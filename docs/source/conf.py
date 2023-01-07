import sphinx_rtd_theme
# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'EasyCord'
copyright = '2023, EgogorGames'
author = 'EgogorGames'

release = '0.1'
version = '1.1.3'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_themes']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output

epub_show_urls = 'footnote'

# -- Theme options

html_theme_options = {
    'analytics_id': 'G-RQEPS29B0D',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'gray',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'github_url': 'https://github.com/EgogorGames/EasyCord/',
    'html-logo': 'LogoSmall_195x45.png'
}

