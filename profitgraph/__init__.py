"Small program that creates graphs based on date, profit or purchases"

from . import main

def start_program():
    graph = main.Mode()
    graph.select()

__project__      = 'profitgraph'
__version__      = '0.8.0'
__keywords__     = ['profits', 'graphs', 'analytics']
__author__       = 'Morjovski'
__author_email__ = 'amor3ux@gmail.com'
__url__          = 'https://github.com/Morjovski/profit_graph'
__platforms__    = 'ALL'

__classifiers__ = [
    "Development Status :: 4 - Beta",
    "Topic :: Utilities",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

__entry_points__ = {
    'console_scripts': [
        'startgraph = profitgraph.__init__:start_program',
    ],
}

__requires__ = [
        'matplotlib~=3.6.2',
        'mplcursors~=0.5.2',
        'tqdm~=4.64.1',
        'colorama~=0.4.6',
    ]