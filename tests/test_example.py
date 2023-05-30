"""Unit test package for pdfgpt."""
from pdfgpt import *

d = PDFBot(openai_key='OPENAI_KEY')

print('Example')
extracted_text, num_pages = d.generateText(file_path='epanet_matlab_toolkit.pdf')
df = d.generateEmbeddings(extracted_text)

print('USER: What is EPANET?')
prompt = d.generatePrompt(df, num_pages, 'What is EPANET?')
response = d.sendPrompt(prompt, model="gpt-3.5-turbo")
print('AI')
print(response, '\n')

print('USER: Give me a minimum example code?')
prompt = d.generatePrompt(df, num_pages, 'Give me the command to load a network?')
response = d.sendPrompt(prompt, model="gpt-3.5-turbo", temperature=0.9)
print('AI')
print(response)

