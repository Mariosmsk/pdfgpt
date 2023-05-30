#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'openai', 'pandas', 'pypdf', 'matplotlib', 'plotly', 'scipy', 'scikit-learn', 'tiktoken']

test_requirements = []

setup(
    author="Marios S. Kyriakou",
    author_email='kiriakou.marios@ucy.ac.cy',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="pdfgpt is a Python package that provides users with the ability to engage in natural language "
                "conversations with their PDF documents.",
    entry_points={
        'console_scripts': [
            'pdfgpt=pdfgpt.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pdfgpt',
    name='pdfgpt',
    packages=find_packages(include=['pdfgpt', 'pdfgpt.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Mariosmsk/pdfgpt',
    version='0.2.1',
    zip_safe=False,
)
