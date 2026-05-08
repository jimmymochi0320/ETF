from translators.base_translator import BaseTranslator
class DeepLTranslator(BaseTranslator):
    def __init__(self, api_key:str): self.api_key=api_key
    def translate(self,text:str)->str:
        try:
            import deepl
            t=deepl.Translator(self.api_key)
            return t.translate_text(text,target_lang='ZH-HANT').text
        except Exception:
            return text
