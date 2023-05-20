======
pdfgpt
======


.. image:: https://img.shields.io/pypi/v/pdfgpt.svg
        :target: https://pypi.python.org/pypi/pdfgpt

.. image:: https://readthedocs.org/projects/pdfgpt/badge/?version=latest
        :target: https://pdfgpt.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

.. image:: https://pepy.tech/badge/pdfgpt
        :target: https://pepy.tech/badge/pdfgpt
        :alt: Downloads

.. image:: https://pepy.tech/badge/pdfgpt/month
        :target: https://pepy.tech/badge/pdfgpt
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
    extracted_text, num_pages = d.generateText(file_path='PDF_NAME.pdf')
    df = d.generateEmbeddings(extracted_text)

    print('USER')
    prompt = d.generatePrompt(df, num_pages, 'what is the epanet?')
    response = d.sendPrompt(prompt)
    print('AI')
    print(response)

    print('USER')
    prompt = d.generatePrompt(df, num_pages, 'Give me an example get the node elevations with matlab code?')
    response = d.sendPrompt(prompt)
    print('AI')
    print(response)

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
