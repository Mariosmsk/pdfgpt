"""Unit test package for pdfgpt."""
from pdfgpt import *

d = PDFBot(openai_key='OPENAI_KEY')

print('Example')
extracted_text, num_pages = d.generateText(file_path='epanet_matlab_toolkit.pdf')
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

