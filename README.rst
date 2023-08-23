======
pdfgpt
======


.. image:: https://img.shields.io/pypi/v/pdfgpt.svg
        :target: https://pypi.python.org/pypi/pdfgpt

.. image:: https://readthedocs.org/projects/pdfgpt/badge/?version=latest
        :target: https://pdfgpt.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

.. image:: https://static.pepy.tech/badge/pdfgpt
        :target: https://pepy.tech/badge/pdfgpt
        :alt: Downloads

.. image:: https://static.pepy.tech/badge/pdfgpt/month
        :target: https://pepy.tech/badge/pdfgpt/month
        :alt: Downloads

pdfgpt is a Python package that provides users with the ability to engage in natural language conversations with their PDF documents.


* Free software: MIT license
* Documentation: https://pdfgpt.readthedocs.io.

**Source:** Openai - https://github.com/openai/openai-cookbook

How to install
---------------

**Environments -> base (root) -> open terminal -> pip install pdfgpt**

* pip install pdfgpt

Example
-------

.. code-block:: python

    from pdfgpt import *

    d = PDFBot(openai_key='OPENAI_KEY')

    print('Example')
    extracted_text, num_pages = d.generateText(file_path='tests/epanet_matlab_toolkit.pdf')
    df = d.generateEmbeddings(extracted_text)

    print('USER: What is EPANET?')
    prompt = d.generatePrompt(df, num_pages, 'What is EPANET?')
    response = d.sendPrompt(prompt, model="gpt-3.5-turbo")
    print('AI')
    print(response, '\n')

What is EPANET?

EPANET is a software for modeling water distribution systems' hydraulic and quality dynamics, initially developed by the US Environmental Protection Agency in the C programming language in 1994. It uses a geometric representation of the pipe network, along with a set of initial conditions, rules of operation, and uses this information to compute flows, pressures, and water quality throughout the network, for a certain period of time.

.. code-block:: python

    print('USER: Give me the command to load a network?')
    prompt = d.generatePrompt(df, num_pages, 'Give me the command to load a network?')
    response = d.sendPrompt(prompt, model="gpt-3.5-turbo", temperature=0.9)
    print('AI')
    print(response)

What is the command to load a network?

The command to load a network is:

G = epanet( ’BWSN_Network_1 .inp’);%Load EPANET Input file

G.loadMSXFile( ’Arsenite .msx’);%Load MSX file

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
