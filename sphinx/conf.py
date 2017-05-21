import sphinx_bootstrap_theme

from opcodes import __version__

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

source_suffix = '.rst'
master_doc = 'index'

project = 'CPU Opcodes'
copyright = '2014-2017, Georgia Institute of Technology'

version = __version__
release = __version__

pygments_style = 'sphinx'

html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
