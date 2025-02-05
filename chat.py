import os
import pandas as pd
import time
import google.generativeai as genai

# Initialize the Google Generative AI model

def setup():
    genai.configure(api_key="AIzaSyD_JLFtabbujqdLsmSACpdHOHyTBmHL4fQ")
    model = genai.GenerativeModel('gemini-pro')
    return model

INITIAL_PROMPT = ('''
    You are a career counselor..
''')

def get_response(prompt):
    model = setup()
    full_prompt = INITIAL_PROMPT + prompt
    response = model.generate_content(full_prompt)
    return response.text

# Example usage
response = get_response("What career advice can you give me?")
print(response)
