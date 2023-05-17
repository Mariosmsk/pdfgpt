"""Main module."""
import openai
import pandas as pd
from pypdf import PdfReader
from openai.embeddings_utils import get_embedding, cosine_similarity


def split_text_to_pages(text, max_length=2000):
    pages = []
    current_page = ''
    for line in text.split('\n'):
        if len(current_page) + len(line) + 1 > max_length:
            pages.append(current_page.strip())
            current_page = ''
        current_page += line + '\n'
    if current_page:
        pages.append(current_page.strip())
    return pages


def extract_any_text(df):
    string_columns = list(df.keys())
    text_column = df[string_columns].apply(lambda x: ' '.join([str(x[col]) for col in x.index]), axis=1)
    extracted_text = ' '.join(text_column.tolist())
    extracted_text = split_text_to_pages(extracted_text)
    extracted_text = [{'text': page_text} for page_text in extracted_text if page_text.strip() != '']
    num_pages = len(extracted_text)
    return extracted_text, num_pages


class PDFBot:

    def __init__(self, openai_key):
        openai.api_key = openai_key
        self.cnt = 4000

    # Extract text from PDFs
    def generateText(self, file_path=None, df=None):
        extracted_text = []
        if df is not None:
            extracted_text, num_pages = extract_any_text(df)
            return extracted_text, num_pages

        pdf_document = PdfReader(file_path)
        num_pages = len(pdf_document.pages)

        for page_num in range(num_pages):
            processed_text = []
            current_font_size = None
            current_blob_text = ''
            page = pdf_document.pages[page_num]
            page_text = page.extract_text()
            page_text = [
                {'font_size': None, 'text': page_text, 'x_coord': None,
                 'y_coord': None}] if page_text is not None else []

            for text in page_text:
                if text['font_size'] == current_font_size:
                    current_blob_text += f" {text['text']}"
                    if len(current_blob_text) >= 2000:
                        processed_text.append({
                            'font_size': current_font_size,
                            'text': current_blob_text,
                            'page': page_num
                        })
                        current_font_size = None
                        current_blob_text = ''
                else:
                    if current_font_size is not None and len(current_blob_text) >= 1:
                        processed_text.append({
                            'font_size': current_font_size,
                            'text': current_blob_text,
                            'page': page_num
                        })
                    current_font_size = text['font_size']
                    current_blob_text = text['text']
            extracted_text += processed_text
        return extracted_text, num_pages

    # Generate embeddings from PDFs
    def generateEmbeddings(self, extracted_text='', model_embeddings="text-embedding-ada-002"):
        filtered_text = [row for row in extracted_text if len(row['text']) >= 30]
        unique_text = [dict(t) for t in {tuple(d.items()) for d in filtered_text}]
        df = pd.DataFrame(unique_text)
        df['text'] = df['text'].str.slice(stop=26000)
        df['text_length'] = df['text'].str.len()
        embeddings = df.text.apply(lambda x: get_embedding(x, engine=model_embeddings))
        df["embeddings"] = embeddings
        return df

    # Generate prompt based on embeddings
    def generatePrompt(self, df, num_pages, message, model_embeddings="text-embedding-ada-002"):
        query_embedding = get_embedding(message, engine=model_embeddings)
        similarities = cosine_similarity(df.embeddings.tolist(), query_embedding)
        result_indices = similarities.argsort()[::-1][:num_pages]
        df['text'].array[0] = df['text'].array[0][:self.cnt]
        result = df.iloc[result_indices]

        index = min(len(result), 3) - 2
        len_res = len(result)

        prompt = f"""Given the question: {message} and the following embeddings as data:
                    1. {result.iloc[index]['text']}
                    2. {result.iloc[(index + 1) % len_res]['text']}
                    3. {result.iloc[(index + 2) % len_res]['text']}
                    Give an answer based only on the data where I provide or return not available information.
                    """
        return prompt

    # Sends a prompt to the OpenAI API and return the response
    def sendPrompt(self, prompt, model="text-davinci-003", temperature=0.4, max_tokens=1250, frequency_penalty=0.0,
                   top_p=1, presence_penalty=0.6):
        response = openai.Completion.create(model=model, prompt=prompt, temperature=temperature,
                                            max_tokens=max_tokens, top_p=top_p, frequency_penalty=frequency_penalty,
                                            presence_penalty=presence_penalty)
        return response.choices[0]['text']
