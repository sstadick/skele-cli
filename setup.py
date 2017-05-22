"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join

from setuptools import find_packages, setup

from skele import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name = 'skele',
    version = __version__,
    description = 'A skeleton command line program in Python.',
    long_description = long_description,
    author = 'Seth Stadick',
    author_email = 'sstadick@personalgenome.com',
    license = 'UNLICENSE',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['click'],
    entry_points = {
        'console_scripts': [
            'skele=skele.cli:main',
        ],
    }
)
