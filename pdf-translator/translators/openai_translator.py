from translators.base_translator import BaseTranslator

class OpenAITranslator(BaseTranslator):
    def __init__(self, api_key:str, model:str='gpt-4.1-mini'):
        self.api_key=api_key; self.model=model
    def translate(self,text:str)->str:
        try:
            from openai import OpenAI
            client=OpenAI(api_key=self.api_key)
            r=client.chat.completions.create(model=self.model,messages=[
                {"role":"system","content":"你是一位專業學術翻譯員。請將英文學術論文內容翻譯為繁體中文並只輸出譯文。"},
                {"role":"user","content":text}
            ])
            return r.choices[0].message.content.strip()
        except Exception:
            return text
