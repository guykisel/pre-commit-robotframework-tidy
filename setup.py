#!/usr/bin/env python

import sys

from setuptools import find_packages, setup

install_requires = ['robotframework']
if sys.version_info < (2, 7):
    install_requires.append('argparse')


setup(
    name='pre_commit_robotframework_tidy',
    description='A pre-commit hook to run Robot Framework\'s tidy tool.',
    url='https://github.com/guykisel/pre-commit-robotframework-tidy',
    version='0.0.1dev0',
    author='Guy Kisel',
    author_email='guy.kisel@gmail.com',
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
    ],
    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'python-robotframework-tidy = pre_commit_hook.rf_tify:main',
        ],
    },
)
