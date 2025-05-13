# API는 '프로그램 사용법'
import deepl
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
df = pd.read_excel(r'Part3\english.xlsx')
api_key = os.getenv('deepL_api')

translator = deepl.Translator(api_key)

df.drop(columns=['korean'])

translated = df['english'].apply(lambda text: translator.translate_text(str(text), target_lang="KO").text)
df['korean'] = translated

df.to_excel(r'Part3\translated_output.xlsx')