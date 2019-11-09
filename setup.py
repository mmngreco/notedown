from __future__ import absolute_import
import subprocess

from setuptools import setup

setup(
    name="notedown",
    version="1.5.1",
    description="Convert markdown to IPython notebook.",
    packages=['notedown'],
    author="Aaron O'Leary",
    author_email='dev@aaren.me',
    license='BSD 2-Clause',
    url='http://github.com/aaren/notedown',
    install_requires=['nbformat',
                      'nbconvert',
                      'pandoc-attributes',
                      'six'],
    entry_points={'console_scripts': ['notedown = notedown.main:app', ]},
    package_dir={'notedown': 'notedown'},
    package_data={'notedown': ['templates/markdown.tpl',
                               'templates/markdown_outputs.tpl']},
    include_package_data=True,
)
